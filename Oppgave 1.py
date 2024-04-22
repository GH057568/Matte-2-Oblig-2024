

import math

hs = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001, 0.000000000001, 0.0000000000001   ]
def calculate_derivative(hs):
    p = 1.5
    b=0.1
    n=0
    for n in range(1):
        n+=1
        f = (math.e ** (p + hs) - math.e ** (p-hs)) / 2*hs
        print("h =", h, ", f =", f)
        b /= 10  


for h in hs:
    print("Experiment with h =", h)
    calculate_derivative(h)
    print("-----------------------------")

