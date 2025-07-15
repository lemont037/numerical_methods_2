import math

class Expression:
    def __init__(self, func_str, variable='x'):
        """
        Initializes the Equation object with a function string and variable name.
            - func_str (str): A string representing the mathematical function, e.g., "x**2 + 3*x".
            - variable (str, optional): The variable used in the function. Defaults to 'x'.
        Attributes:
            - func_str (str): Stores the function string.
            - variable (str): Stores the variable name.
            - func (callable): A lambda function generated from func_str and variable.
        Raises:
            - Exception: If func_str is invalid or cannot be evaluated as a function.
        """
        self.func_str = func_str
        self.variable = variable
        self.func = eval(f"lambda {variable}: {func_str}")

    def __call__(self, x):
        return self.func(x)

    def __str__(self):
        return self.func_str