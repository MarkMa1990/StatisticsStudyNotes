# This is to test/demonstrate the Central Limit Theorem (CLT)
# example of Lyapunov CLT

# Author: Hongfeng Ma, Jan. 2024, Denmark

import numpy as np
import matplotlib.pyplot as plt

#  number of experiments
Nexp = 10000

# x_avg_all, storage the average measurement of each experiment
x_avg_all = np.zeros(Nexp)
for i0 in range(Nexp):
    np.random.seed(np.random.randint(1,1e9,size=1))
    
    N = 10
    #mu = 1
    #sigma = 0.5
    #x = np.random.normal(mu,sigma,N)
    #np.random.seed(np.random.randint(1,1000,size=1))
    x = np.random.random(N)
    
    mu_exp = np.mean(x)
    #sigma_exp = np.std(x,ddof=1)
    
    x_avg_all[i0]=mu_exp

x = np.float32(x_avg_all)

#print(abs(mu - np.mean(x)),abs(sigma-np.std(x,ddof=1)))

hist, edges = np.histogram(x,bins=100,)

plt.figure()
plt.bar(edges[0:-1],hist,align='center',width=1/500)

plt.figure()
plt.boxplot(x,
    vert=True,  # vertical box alignment
    patch_artist=False,  # fill with color
    )
plt.show()
