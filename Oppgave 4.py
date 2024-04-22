import numpy as np
import matplotlib.pyplot as plt


L = 1.0  
time = 0.1  


h_values = [0.01, 0.02, 0.03, 0.04, 0.05,]
k_values = [0.00001, 0.00005, 0.0001, 0.0005]


for h in h_values:
    for k in k_values:
       
        if k / h**2 > 0.5:
            print(f"Kombinasjonen h={h} og k={k} er ikke stabil.")
            continue
        
        nx = int(L / h) + 1  
        nt = int(time / k)  

    
        u = np.zeros(nx)
        u[int(nx / 2)] = 100  

        
        for n in range(nt):
            u_next = np.copy(u)  
            for i in range(1, nx - 1):
                u_next[i] = u[i] + (k / h**2) * (u[i + 1] - 2 * u[i] + u[i - 1])
            u = u_next
        
       
        plt.plot(np.linspace(0, L, nx), u, label=f"h={h}, k={k}")

plt.xlabel('Lengde (m)')
plt.ylabel('Temperatur (C)')
plt.title('Temperaturfordeling etter simulering')
plt.legend()
plt.show()