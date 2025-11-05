import json
import tkinter as tk
from tkinter import ttk, messagebox
from functools import partial
import numpy as np
from scipy.optimize import linprog

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except Exception:
    HAS_MPL = False


HELP_TEXT = (
    "Maximize Z = c1*x1 + c2*x2\n"
    "All constraints are of the form: a1*x1 + a2*x2 ≤ b (leave a row blank to skip).\n"
    "Variables x1, x2 are constrained to be ≥ 0.\n\n"
    "Tip: Load a preset from the dropdown to auto-fill an example."
)


class LPSolverGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LP Solver (Simplex/HiGHS) – Maximize c1*x1 + c2*x2")
        self.geometry("660x520")
        self.resizable(False, False)

        top_frame = tk.Frame(self)
        top_frame.pack(padx=10, pady=(10, 4), fill="x")

        tk.Label(top_frame, text="Preset:").pack(side="left")
        self.preset_var = tk.StringVar(value="— choose a preset —")
        self.preset_combo = ttk.Combobox(
            top_frame, textvariable=self.preset_var,
            values=list(DEFAULT_PRESETS.keys()), width=28, state="readonly"
        )
        self.preset_combo.pack(side="left", padx=6)
        ttk.Button(top_frame, text="Load", command=self.load_preset).pack(side="left", padx=4)
        ttk.Button(top_frame, text="Help", command=self.show_help).pack(side="right")

        obj_frame = tk.LabelFrame(self, text="Objective: Maximize Z = c1*x1 + c2*x2")
        obj_frame.pack(padx=10, pady=8, fill="x")

        self.c1_var = tk.StringVar(value="")
        self.c2_var = tk.StringVar(value="")
        tk.Label(obj_frame, text="c1").grid(row=0, column=0, padx=6, pady=6, sticky="e")
        tk.Entry(obj_frame, textvariable=self.c1_var, width=10).grid(row=0, column=1, padx=6, pady=6)
        tk.Label(obj_frame, text="c2").grid(row=0, column=2, padx=6, pady=6, sticky="e")
        tk.Entry(obj_frame, textvariable=self.c2_var, width=10).grid(row=0, column=3, padx=6, pady=6)

        cons_frame = tk.LabelFrame(self, text="Constraints (a1*x1 + a2*x2 ≤ b)")
        cons_frame.pack(padx=10, pady=8, fill="x")

        headers = ["a1", "a2", "b"]
        for j, h in enumerate(headers):
            tk.Label(cons_frame, text=h, font=("TkDefaultFont", 9, "bold")).grid(row=0, column=j, padx=8, pady=4)

        self.rows = []
        for i in range(5):
            a1 = tk.StringVar(value="")
            a2 = tk.StringVar(value="")
            b = tk.StringVar(value="")
            self.rows.append((a1, a2, b))
            tk.Entry(cons_frame, textvariable=a1, width=10).grid(row=i+1, column=0, padx=6, pady=4)
            tk.Entry(cons_frame, textvariable=a2, width=10).grid(row=i+1, column=1, padx=6, pady=4)
            tk.Entry(cons_frame, textvariable=b, width=12).grid(row=i+1, column=2, padx=6, pady=4)

        btn_frame = tk.Frame(self)
        btn_frame.pack(padx=10, pady=10, fill="x")

        ttk.Button(btn_frame, text="Solve", command=self.solve).pack(side="left")
        if HAS_MPL:
            ttk.Button(btn_frame, text="Plot (2D)", command=self.plot_solution).pack(side="left", padx=8)
        else:
            ttk.Button(btn_frame, text="Plot (2D)", state="disabled").pack(side="left", padx=8)

        ttk.Button(btn_frame, text="Clear", command=self.clear_all).pack(side="left", padx=8)

        self.result_box = tk.Text(self, height=12, width=80)
        self.result_box.pack(padx=10, pady=(0,10))
        self.result_box.configure(state="disabled")

        footer = tk.Label(self, text="Note: x1, x2 ≥ 0 is enforced automatically (HiGHS).", fg="#666")
        footer.pack(pady=(0, 8))

    def show_help(self):
        messagebox.showinfo("Help", HELP_TEXT)

    def clear_all(self):
        self.c1_var.set("")
        self.c2_var.set("")
        for a1, a2, b in self.rows:
            a1.set(""); a2.set(""); b.set("")
        self.write_result("Cleared.\n")

    def write_result(self, text):
        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("end", text)
        self.result_box.configure(state="disabled")

    def load_preset(self):
        name = self.preset_var.get()
        data = DEFAULT_PRESETS.get(name, {})
        if not data:
            return
        c = data.get("c", [None, None])
        A = data.get("A", [])
        b = data.get("b", [])
        self.c1_var.set("" if c[0] is None else str(c[0]))
        self.c2_var.set("" if c[1] is None else str(c[1]))
        for a1, a2, bb in self.rows:
            a1.set(""); a2.set(""); bb.set("")
        for i, (row, bi) in enumerate(zip(A, b)):
            if i >= len(self.rows):
                break
            self.rows[i][0].set(str(row[0]))
            self.rows[i][1].set(str(row[1]))
            self.rows[i][2].set(str(bi))
        self.write_result(f"Loaded preset: {name}\n")

    def collect_inputs(self):
        try:
            c1 = float(self.c1_var.get().strip())
            c2 = float(self.c2_var.get().strip())
        except Exception:
            raise ValueError("Objective coefficients c1 and c2 must be numbers.")
        c = np.array([-c1, -c2], dtype=float)  # negate for maximize

        A_list, b_list = [], []
        for (a1, a2, b) in self.rows:
            s1, s2, sb = a1.get().strip(), a2.get().strip(), b.get().strip()
            if not s1 and not s2 and not sb:
                continue  # skip empty row
            try:
                A_list.append([float(s1), float(s2)])
                b_list.append(float(sb))
            except Exception:
                raise ValueError("Each non-empty constraint row must contain numeric a1, a2, b.")

        if len(A_list) == 0:
            raise ValueError("Enter at least one constraint row (a1, a2, b).")

        A_ub = np.array(A_list, dtype=float)
        b_ub = np.array(b_list, dtype=float)

        return c, A_ub, b_ub

    def solve(self):
        try:
            c, A_ub, b_ub = self.collect_inputs()
            bounds = [(0, None), (0, None)]  # x1 >= 0, x2 >= 0

            res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
            if not res.success:
                self.write_result(
                    "❌ Optimization failed.\n"
                    f"Status: {res.status} | {res.message}\n"
                    "Check your inputs (infeasible or unbounded problems are possible)."
                )
                return

            x1, x2 = res.x
            zmax = -res.fun 
            report = []
            report.append("✅ Optimal solution found (HiGHS):\n")
            report.append(f"x1 = {x1:.6g}\n")
            report.append(f"x2 = {x2:.6g}\n")
            report.append(f"Zmax = {zmax:.6g}\n")
            report.append("\nKKT / Solver info:\n")
            report.append(f"Iterations: {res.nit}\n")
            report.append(f"Status code: {res.status} | {res.message}\n")
            self.write_result("".join(report))

            self._last_solution = (A_ub, b_ub, x1, x2)
        except Exception as e:
            messagebox.showerror("Input error", str(e))

    def plot_solution(self):
        if not HAS_MPL:
            messagebox.showwarning("Plot disabled", "matplotlib is not installed.")
            return
        if not hasattr(self, "_last_solution"):
            messagebox.showinfo("No solution", "Solve the problem first.")
            return

        A_ub, b_ub, x1_opt, x2_opt = self._last_solution
        xs = np.linspace(0, max(1, x1_opt * 1.3 + 5), 400)

        plt.figure()
        for (a1, a2), b in zip(A_ub, b_ub):
            if abs(a2) < 1e-12:
                if abs(a1) > 1e-12:
                    x_line = b / a1
                    plt.axvline(x_line, linestyle="--")
            else:
                ys = (b - a1 * xs) / a2
                plt.plot(xs, ys, linestyle="--")

        plt.scatter([x1_opt], [x2_opt], label="Optimum", zorder=5)
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.xlabel("x1"); plt.ylabel("x2")
        plt.title("Constraints (≤) and optimal solution")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()


def main():
    app = LPSolverGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
