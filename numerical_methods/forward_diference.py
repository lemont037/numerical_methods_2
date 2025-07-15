"""
forward_difference.py

Implementation of the forward difference method for numerical approximation of derivatives.
    - Forward Difference Method: Approximates the first derivative of a function at a given point using the forward difference formula.

Usage example available in the main block (__main__).
"""

def forward_difference(f, x, h):
    """
    Forward Difference Method.
    f  : function f(x)
    x  : point at which to evaluate the derivative.
    h  : step size.
    Returns: the approximate value of the derivative of f at point x.
    """
    
    return (f(x+h) - f(x)) / h