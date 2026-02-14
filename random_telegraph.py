import numpy as np
import matplotlib.pyplot as plt

gamma = 1.0
Tmax = 20

t = 0
y = 1

times = [t]
states = [y]

while t < Tmax:
    tau = -np.log(np.random.rand()) / gamma
    t += tau
    y = -y
    
    times.append(t)
    states.append(y)

plt.step(times, states)
plt.xlabel("t")
plt.ylabel("Y(t)")
plt.title("Random Telegraph Process")
plt.show()
