import numpy as np
import matplotlib.pyplot as plt

alpha = 2
beta = 1
KR = 1
n = 2
Omega = 50
Steps = 100000

def gR(x):
    return 1 / (1 + (x/KR)**n)

S = np.array([[1,0,-1,0], [0,1,0,-1]])

r1, r2, t = 10, 40, 0
r1_list, r2_list, t_list = [r1], [r2], [t]

for i in range(Steps):
    nu = np.array([alpha*gR(r2/Omega), alpha*gR(r1/Omega), 
                   beta*r1/Omega, beta*r2/Omega])
    a = np.sum(nu)
    if a == 0: break
    
    tau = -np.log(np.random.rand()) / a
    t += tau
    mu = np.searchsorted(np.cumsum(nu)/a, np.random.rand())
    
    r1 += S[0,mu]
    r2 += S[1,mu]
    
    r1_list.append(r1)
    r2_list.append(r2)
    t_list.append(t)

plt.plot(t_list, r1_list, label="r1")
plt.plot(t_list, r2_list, label="r2")
plt.legend()
plt.show()
