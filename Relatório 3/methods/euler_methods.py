from forward_diference import forward_difference as foward

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

def euler_explicit(f, y0, t0, tf, h):
    """
    Explicit Euler method for ODEs.
    f  : function f(t, y)
    y0 : initial value
    t0 : initial time
    tf : final time
    h  : step size
    Returns: lists of t and y
    """
    return y0 + (tf-t0) * foward(f, y0, h)

def euler_implicit(f, y0, t0, tf, h, solver=None):
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
    pass

def euler_modified(f, y0, t0, tf, h):
    """
    Modified Euler method (Euler-Cromer or Heun) for ODEs.
    f  : function f(t, y)
    y0 : initial value
    t0 : initial time
    tf : final time
    h  : step size
    Returns: lists of t and y
    """
    pass

if __name__ == "__main__":
    # Example usage of Euler functions
    def f(t, y):
        return -y + 1

    y0 = 0
    t0 = 0
    tf = 5
    h = 0.1

    print("Explicit Euler:")
    t_exp, y_exp = euler_explicit(f, y0, t0, tf, h)
    print(list(zip(t_exp, y_exp)))

    print("\nImplicit Euler:")
    # Simple solver example for linear equation
    def solver(g, y_guess):
        # g(y) = y - h*f(t+h, y) - y_prev = 0
        # For f(t, y) = -y + 1, we have: y - h*(-y + 1) - y_prev = 0
        # y + h*y - h - y_prev = 0 => y*(1 + h) = y_prev + h => y = (y_prev + h)/(1 + h)
        return (y_guess[0] + h) / (1 + h)

    t_imp, y_imp = euler_implicit(f, y0, t0, tf, h, solver=solver)
    print(list(zip(t_imp, y_imp)))

    print("\nModified Euler (Heun):")
    t_mod, y_mod = euler_modified(f, y0, t0, tf, h)
    print(list(zip(t_mod, y_mod)))
