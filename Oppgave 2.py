# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:07:49 2024

@author: Alexander Lyle
"""

import sympy as sp

x = sp.Symbol('x')

def taylor_series(func, x0, n, h):
    f = func.subs(x, x0)
    taylor_series = f
    for i in range(1, n+1):
        derivative = func.diff(x, i).subs(x, x0)
        taylor_series += (derivative * h**i) / sp.factorial(i)
    return taylor_series

p = 1.5
n = 13
hs = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001, 0.000000000001, 0.0000000000001]

func = sp.exp(x)

taylor_series_results = []
for h in hs:
    taylor = taylor_series(func, p, n, h)
    taylor_series_results.append(taylor)

print("Taylor series expansions:")
for i, taylor in enumerate(taylor_series_results):
    print(f"For h = {hs[i]}:")
    print(taylor)
