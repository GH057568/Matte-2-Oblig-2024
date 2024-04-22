import numpy as np
import matplotlib.pyplot as plt

L = 2 * np.pi  
time = 0.1  
alpha = 0.1  
h = L / 100  
k = 0.001  

nx = int(L / h)
nt = int(time / k)

x = np.linspace(0, L, nx)
initial_profile = np.sin(x)

def analytical_solution(x, t):
    return np.exp(-alpha * t) * np.sin(x)

def explicit_method(u, nx, nt, h, k):
    for n in range(nt):
        u_next = np.copy(u)
        for i in range(1, nx - 1):
            u_next[i] = u[i] + alpha * k / h**2 * (u[i + 1] - 2 * u[i] + u[i - 1])
        u = u_next
    return u

def implicit_method(u, nx, nt, h, k):
    A = np.zeros((nx, nx))
    for i in range(1, nx - 1):
        A[i, i - 1] = -alpha * k / h**2
        A[i, i] = 1 + 2 * alpha * k / h**2
        A[i, i + 1] = -alpha * k / h**2
    A[0, 0] = 1
    A[-1, -1] = 1
    for n in range(nt):
        B = u.copy()
        u = np.linalg.solve(A, B)
    return u

def crank_nicolson_method(u, nx, nt, h, k):
    A = np.zeros((nx, nx))
    B = np.zeros((nx, nx))
    for i in range(1, nx - 1):
        A[i, i - 1] = -alpha * k / (2 * h**2)
        A[i, i] = 1 + alpha * k / h**2
        A[i, i + 1] = -alpha * k / (2 * h**2)
        
        B[i, i - 1] = alpha * k / (2 * h**2)
        B[i, i] = 1 - alpha * k / h**2
        B[i, i + 1] = alpha * k / (2 * h**2)
    
    A[0, 0] = 1
    A[-1, -1] = 1
    B[0, 0] = 1
    B[-1, -1] = 1

    for n in range(nt):
        u = np.linalg.solve(A, np.dot(B, u))
    return u

u_explicit = initial_profile.copy()
u_implicit = initial_profile.copy()
u_crank_nicolson = initial_profile.copy()

u_explicit = explicit_method(u_explicit, nx, nt, h, k)
u_implicit = implicit_method(u_implicit, nx, nt, h, k)
u_crank_nicolson = crank_nicolson_method(u_crank_nicolson, nx, nt, h, k)

u_analytical = analytical_solution(x, time)

plt.figure(figsize=(12, 8))

plt.plot(x, u_explicit, label='Explisitt metode', linestyle='--')

plt.plot(x, u_implicit, label='Implisitt metode', linestyle='-.')

plt.plot(x, u_crank_nicolson, label='Crank-Nicolson metode', linestyle='-')

plt.plot(x, u_analytical, label='Analytisk løsning', linestyle=':', color='black')

plt.xlabel('Lengde (m)')
plt.ylabel('Temperatur (C)')
plt.title('Sammenligning av eksplisitt, implisitt og Crank-Nicolson-metoder')
plt.legend()
plt.show()

error_explicit = np.abs(u_explicit - u_analytical)
error_implicit = np.abs(u_implicit - u_analytical)
error_crank_nicolson = np.abs(u_crank_nicolson - u_analytical)

plt.figure(figsize=(12, 8))plt.plot(x, error_explicit, label='Feil for eksplisitt metode', linestyle='--')
plt.plot(x, error_implicit, label='Feil for implisitt metode', linestyle='-.')
plt.plot(x, error_crank_nicolson, label='Feil for Crank-Nicolson metode', linestyle='-')
plt.xlabel('Lengde (m)')
plt.ylabel('Feil (C)')
plt.title('Feil for forskjellige numeriske metoder sammenlignet med analytisk løsning')
plt.legend()
plt.show()

