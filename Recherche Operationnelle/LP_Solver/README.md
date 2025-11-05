# 🧮 Linear Programming Solver (Recherche Opérationnelle Project)

A small interactive Python program that solves **linear programming (LP)** problems with two variables using the **Simplex / HiGHS** algorithm from SciPy.  
It provides a clean graphical interface where the user can enter all coefficients manually and instantly get the optimal solution and an optional 2D plot.

---

## 🎯 Objective

The goal of this project is to show how the concepts learned in **Recherche Opérationnelle** — formulation of linear programs, feasible regions, and simplex optimization — can be turned into an actual working computational tool.

This project bridges theory and practice:
- You input the mathematical model parameters.
- The program converts them into standard LP form.
- It solves the optimization problem algorithmically and shows the result.

---

## 🧩 Features

- **Manual input interface:** enter all coefficients yourself (no predesigned problems)
- Solve LPs of the form  
  **Maximize** `Z = c1*x1 + c2*x2`  
  subject to constraints `a1*x1 + a2*x2 ≤ b`
- Supports up to **five constraints**
- Enforces `x1 ≥ 0`, `x2 ≥ 0`
- Displays:
  - Optimal `x1`, `x2`, and `Zmax`
  - Solver status and iteration count
- Optional **2D plot** of constraints and optimal point
- Packaged as a **stand-alone executable (.exe)** — can run without Python

---

## ⚙️ Installation and Execution

### ▶️ Run with Python (for testing or editing)

1. **Navigate to the project folder:**
   ```bash
   cd "/path/to/LP_Solver_Project"
2. **Create a virtual environment and activate it:**
    python3 -m venv .venv
    source .venv/bin/activate      # macOS / Linux
    .venv\Scripts\Activate         # Windows
3. **Install required libraries:**
    pip install numpy scipy matplotlib
4. **Run the program:**
    python app_gui.py

The application window will open automatically.
