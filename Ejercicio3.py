import numpy as np
import matplotlib.pyplot as plt

m, beta, q, B, kT = 1.0, 1.0, 1.0, 2.0, 1.0
dt, Steps = 0.001, 100000

V = np.zeros((Steps, 3))
sigma = np.sqrt(2*beta*kT/m**2)

for i in range(Steps-1):
    Vx, Vy, Vz = V[i]
    
    V[i+1,0] = Vx + (-beta/m*Vx + q*B/m*Vy)*dt + sigma*np.sqrt(dt)*np.random.randn()
    V[i+1,1] = Vy + (-beta/m*Vy - q*B/m*Vx)*dt + sigma*np.sqrt(dt)*np.random.randn()
    V[i+1,2] = Vz + (-beta/m*Vz)*dt + sigma*np.sqrt(dt)*np.random.randn()

plt.plot(V[:,0], V[:,1])
plt.title("Brownian Motion in Magnetic Field")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.show()
