# Numerical Methods II

This repository contains implementations of numerical methods developed during the **Numerical Methods II** course at the **Universidade Federal do Ceará (UFC)** in the 2025.1 semester.

## 📁 Project Structure
---

```
Relatórios/
├── numerical_methods/          # Main package with implementations
│   ├── __init__.py
│   ├── euler.py               # Euler methods for ODEs
│   ├── forward_diference.py   # Forward finite differences
│   ├── newton_raphson.py      # Newton-Raphson method
│   └── utils/                 # Auxiliary utilities
│       ├── __init__.py
│       ├── equations.py       # Class for expression manipulation
│       └── prints.py          # Table formatting
├── Reports/                   # Reports organized by number
│   └── report_03/
└── README.md
```

## 🧮 Implemented Methods
---

### 1. Euler Methods for Ordinary Differential Equations (ODEs)
- **Explicit Euler**: Direct method for solution approximation
- **Implicit Euler**: Implicit method with greater stability
- **Modified Euler (Heun)**: Second-order predictor-corrector method

### 2. Finite Differences
- **Forward Difference**: Numerical approximation of derivatives using forward differences

### 3. Methods for Nonlinear Equations
- **Newton-Raphson**: Iterative method for finding roots of nonlinear functions

## 🚀 How to Use
---

### Installation
```bash
# Clone the repository
git clone <repository-url>
```

### Usage Example - Euler Method

```python
from numerical_methods.euler import euler_explicit, euler_implicit, euler_modified

# Define the ODE: y' = -y + 1
def f(t, y):
    return -y + 1

# Parameters
y0 = 0      # Initial value
t0 = 0      # Initial time
tf = 5      # Final time
h = 0.1     # Step size

# Explicit Euler
t_values, y_values = euler_explicit(f, y0, t0, h, steps=50)

# Modified Euler (Heun)
t_values, y_values = euler_modified(f, y0, t0, tf, h)
```

### Usage Example - Newton-Raphson

```python
from numerical_methods.newton_raphson import newton_raphson
import math

# Find root of f(x) = x² - 2
def f(x):
    return x**2 - 2

def df(x):  # Derivative
    return 2*x

# Find √2
root = newton_raphson(f, df, x0=1.0, tol=1e-6)
print(f"√2 ≈ {root}")
```

### Usage Example - Utilities

```python
from numerical_methods.utils.prints import print_table
from numerical_methods.utils.equations import Expression

# Table formatting
headers = ["Iteration", "x", "f(x)", "Error"]
data = [
    [1, 1.0, 1.5, 0.5],
    [2, 1.4, 1.414, 0.014],
    [3, 1.414, 1.4142, 0.0002]
]
print_table(headers, data, decimal_places=4)

# Mathematical expression manipulation
expr = Expression("x**2 + 3*x - 5", variable='x')
result = expr(2)  # Calculates f(2)
```

## 📊 Main Features
---

### Table Formatting
- Automatic column alignment
- Decimal places control
- Visual separators for better readability

### Expression Manipulation
- Dynamic evaluation of functions from strings
- Support for complex mathematical functions
- Simple interface for equation creation

### Robust Numerical Methods
- Error and tolerance control
- Configurable parameters
- Handling of special cases

## 🔧 Requirements
---

- Python 3.6+
- Python standard libraries (math)

## 📚 Reports
---

The reports are organized in the `Reports/` folder and include:
- Comparative analysis of methods
- Charts and visualizations
- Discussions on convergence and stability
- Practical application examples

## 🎯 Academic Objectives
---

This project aims to:
- Implement fundamental algorithms of numerical methods
- Compare efficiency and accuracy between different approaches
- Develop reusable tools for numerical analysis
- Apply theoretical concepts to practical problems

## 👨‍💻 Author
---

**Leonardo Monteiro**  
Federal University of Ceará (UFC)  
Course: Numerical Methods II  
Semester: 2025.1

## 📄 License
---

This project is developed for academic purposes as part of the activities of the Numerical Methods II course at UFC.