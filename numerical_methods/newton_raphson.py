"""
newton-raphson.py

Implementation of the Newton-Raphson method for finding roots of nonlinear equations.
    - Newton-Raphson Method: Iteratively approximates the root of a real-valued function using its derivative and an initial guess.

Usage example available in the main block (__main__).
"""

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson Method.
    f        : function f(x)
    df       : derivative of the function f
    x0       : initial guess
    tol      : tolerance for the stopping criterion
    max_iter : maximum number of iterations
    Returns: the approximation of the root x
    """
    
    x = x0
    for n_iter in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Zero derivative. The method failed.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise RuntimeError("Maximum number of iterations exceeded.")

# Example usage:
if __name__ == "__main__":
    # Find root of f(x) = x^2 - 2 (expected root: sqrt(2))
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    root, iterations = newton_raphson(f, df, x0=1.0)
    print(f"Approximate root: {root} in {iterations} iterations")