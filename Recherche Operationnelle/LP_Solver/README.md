# LP Solver  
**Projet Recherche Opérationnelle**

A small interactive Python application that solves **Linear Programming (LP)** problems with two variables using the **Simplex / HiGHS** algorithm from SciPy.  
It provides a clean graphical interface where you can manually enter coefficients and instantly obtain the optimal solution and an optional 2D visualization.

## Folder Structure

```
LP_Solver_Project/
├── app_gui.py           # Main GUI + solver code
├── requirements.txt     # Library dependencies
├── README.md            # Documentation
```

## Features

- Solves problems of the form  
  **Maximize:** `Z = c1*x1 + c2*x2`  
  **Subject to:** `a1*x1 + a2*x2 ≤ b`
- Supports up to **five constraints**
- Enforces non-negativity: `x1 ≥ 0`, `x2 ≥ 0`
- Displays:
  - Optimal values of `x1`, `x2`
  - Maximum value `Zmax`
  - Iteration count and solver status
- Optional **2D plot** of constraints and the optimal point

## Installation and Execution

1. **Open a terminal** and navigate to the project folder:
   ```bash
   cd "/path/to/LP_Solver_Project"
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS / Linux
   .venv\Scripts\Activate         # Windows
   ```

3. **Install required libraries:**
   ```bash
   pip install numpy scipy matplotlib
   ```

4. **Run the application:**
   ```bash
   python app_gui.py
   ```

The application window will open automatically.

## How to Use

1. Enter the coefficients **c1** and **c2** of the objective function.  
2. Fill in each constraint row with coefficients **a1**, **a2**, and the constant **b** for `a1*x1 + a2*x2 ≤ b`.  
   Leave unused rows blank.  
3. Click **Solve** to compute the optimal solution.  
4. Click **Plot (2D)** to visualize the constraints and optimal point.  
5. Click **Clear** to reset all inputs.

## Limitations

- Only **two decision variables** (`x1`, `x2`) for visualization simplicity  
- Constraints must be **≤ type**  
- All variables are **non-negative**  
- No integer or binary decisions  
- Does not display the simplex tableau steps  
- No sensitivity or duality analysis  
- Large coefficients may lead to numerical warnings  
- The 2D plot shows constraint lines and the optimum but not the shaded region

## Technologies Used

- **Python 3.10+**
- **tkinter** – graphical interface  
- **SciPy** – `scipy.optimize.linprog` solver  
- **NumPy** – numerical operations  
- **Matplotlib** – 2D plotting (optional)  
- **PyInstaller** – packaging into `.exe`  

