import sys

from numerical_methods.utils.equations import Expression
from numerical_methods.utils.prints import print_table

from numerical_methods.forward_diference import forward_difference as foward
from numerical_methods.newton_raphson import newton_raphson as newton

"""
euler_methods.py

Implementation of Euler methods for numerical solution of Ordinary Differential Equations (ODEs):
    - Explicit Euler Method
    - Implicit Euler Method
    - Modified Euler Method (Heun/Euler-Cromer)
Each function receives as input the function f(t, y), the initial value y0, the initial time t0, the final time tf, and the step size h.
The implicit method allows passing a solver to solve the resulting nonlinear equation.

Usage example available in the main block (__main__).
"""

def euler_explicit(f, y0, t0, h, s = 1):
    """
    Explicit Euler method for ODEs:
        y = y0 + (tf - t0) * foward(f, y0, t0)
    Parameters:
    f  : function f(t, y)
    y0 : initial value
    t0 : initial time
    h  : step size
    s  : number of steps to run
    Returns: lists of t and y
    """ 
    if s >= 1:
        t = t0 + h
        y = y0 + h * foward(f, y0, h)
        return [(t, y)] + euler_explicit(f, y, t, h, s-1)
    else:
        return []

def euler_implicit(f, df, y0, t0, h, s = 1, solver=newton):
    """
    Implicit Euler method for ODEs.
    f      : function f(t, y)
    y0     : initial value
    t0     : initial time
    tf     : final time
    h      : step size
    solver : function to solve the nonlinear equation (optional)
    Returns: lists of t and y
    """
    if s >= 1:
        t = t0 + h
        y_e = solver(f, df, euler_explicit(f, y0, t0, h)[-1][1])
        y = y0 + h * foward(f, y_e, t)
        return [(t, y)] + euler_implicit(f, df, y, t, h, s-1, solver)
    else:
        return []

if __name__ == "__main__":
    def parse_args(args):
        if len(args) < 7:
            print("Usage: python euler.py <explicit|implicit> <y0> <t0> <h> <s> <f_expr> [<df_expr>]")
            sys.exit(1)
        method = args[1]
        y0 = float(args[2])
        t0 = float(args[3])
        h = float(args[4])
        s = int(args[5])
        f_expr = args[6]
        df_expr = args[7] if method == "implicit" and len(args) > 7 else None
        return method, y0, t0, h, s, f_expr, df_expr

    method, y0, t0, h, s, f_expr, df_expr = parse_args(sys.argv)

    f = Expression(f_expr)
    if method == "explicit":
        result = [(t0, y0)] + euler_explicit(f, y0, t0, h, s)
    elif method == "implicit":
        if not df_expr:
            print("For implicit method, provide derivative expression as the last argument.")
            sys.exit(1)
        df = Expression(df_expr)
        result = [(t0, y0)] + euler_implicit(f, df, y0, t0, h, s)
    else:
        print("Method must be 'explicit' or 'implicit'.")
        sys.exit(1)

    print_table(result)