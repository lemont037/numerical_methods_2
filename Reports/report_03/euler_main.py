import sys
import os
# Adds the parent directory (where "meu_modulo" is located) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from numerical_methods.utils.equations import Expression
from numerical_methods.utils.prints import print_table

from numerical_methods.newton_raphson import newton_raphson as newton
from numerical_methods.euler import euler_explicit, euler_implicit

# Example usage of Euler functions
f = Expression("x**3 * math.exp(-x) + math.sin(x)")
df = Expression("math.exp(-x) * (3 * x**2 - x**3) + math.cos(x)")

y0 = 1
t0 = 0
h = 0.001
s = 50

headers = ["Time", "Explicit Euler", "Implicit Euler"]
print(f"Input:\n  • f : {f}\n  • f': {df}\n  • y0: {y0}\n  • t0: {t0}\n  • h : {h}\n  • s : {s}")

euler_expl_series = euler_explicit(f, y0, t0, h, s)
euler_impl_series = euler_implicit(f, df, y0, t0, h, s, solver=newton)

print("\nResults:")
series = [[t0, y0, y0]]
for i in range(s):
    t_exp, y_exp = euler_expl_series[i]
    t_imp, y_imp = euler_impl_series[i]
    series.append([t_exp, y_exp, y_imp])

print_table(headers, series)