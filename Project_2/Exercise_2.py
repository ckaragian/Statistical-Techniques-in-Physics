from matplotlib import pyplot as plt
import math as mt
import numpy as np
from scipy.stats import norm

N=[10,20,50]

for n in N:
  mean=np.linspace(2,6,100)
  x=np.random.poisson(4,n)
  m=np.mean(x)
  sigma=mt.sqrt(m/n)
  DlnL=n*m*np.log(mean/m)-n*(mean-m)
  plt.plot(mean,DlnL, label="N="+str(n)+", μ $\pm$ σ="+str(round(m,2))+"$\pm$"+str(round(sigma,2)))
plt.xlabel('μ')
plt.ylabel('lnL(μ)-lnL($\hat{μ}$)')
plt.legend()
plt.show()

#Define axes and figures for the histograms
fig, ax = plt.subplots()
fig0, ax0 = plt.subplots()
fig1, ax1 = plt.subplots()

#Define lists to store the values for the histograms
mean=[]
sigma=[]
zeta=[]

#Loop through all N
for n in N:
#Repeat 1000 to generate different N points
 for i in range(1000):
  x=np.random.poisson(4,n)
  m=np.mean(x)
  s=mt.sqrt(m/n)
  #Place the estimation and its error in a list
  mean.append(m)
  sigma.append(s)
  z=(m-4)/s
  zeta.append(z)
 #Fill the histograms
 ax.hist(mean,100, label="N="+str(n)+", mean="+str(round(np.mean(mean),2))+", std="+str(round(np.std(mean),2)))
 ax0.hist(sigma,100, label="N="+str(n)+", mean="+str(round(np.mean(sigma),2)), color='r')
 ax1.hist(zeta,100, label="N="+str(n), color='g')
 ax.set_xlabel('Estimation of maximum likelihood')
 ax.legend()
 ax0.set_xlabel('Error of estimation of maximum likelihood')
 ax0.legend()
 ax1.set_xlabel('z')
 ax1.legend()
 fig.savefig("mean"+str(n)+".png")
 ax.cla()
 fig0.savefig("sigma"+str(n)+".png")
 ax0.cla()
 fig1.savefig("z"+str(n)+".png")
 ax1.cla()
