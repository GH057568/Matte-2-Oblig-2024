import numpy as np
import matplotlib.pyplot as plt

L = 1.0  
time = 0.1  
alpha = 0.01  

h = 0.02  
k = 0.001  

nx = int(L / h) + 1
nt = int(time / k)

u = np.zeros(nx)
u[int(nx / 2)] = 100  

A = np.zeros((nx, nx))
B = np.zeros(nx)

for i in range(1, nx - 1):
    A[i, i - 1] = -alpha * k / h**2
    A[i, i] = 1 + 2 * alpha * k / h**2
    A[i, i + 1] = -alpha * k / h**2

A[0, 0] = 1
A[-1, -1] = 1

for n in range(nt): 
    B[:] = u[:]
    u = np.linalg.solve(A, B)

plt.plot(np.linspace(0, L, nx), u)
plt.xlabel('Lengde (m)')
plt.ylabel('Temperatur (C)')
plt.title('Temperaturfordeling etter simulering')
plt.show()
