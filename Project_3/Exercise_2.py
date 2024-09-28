import math as mt
import numpy as np

x_obs=np.random.rayleigh(10,1)
sigma1=x_obs/0.59
sigma2=x_obs/1.91
print(sigma1,sigma2)

counter=0
for i in range(1000):
x_obs=np.random.rayleigh(10,1)
sigma1=x_obs/0.59
sigma2=x_obs/1.91
if sigma1<=10 or sigma2>=10:
counter+=1
#Calculate percentage
perc=counter/1000
print(perc)
