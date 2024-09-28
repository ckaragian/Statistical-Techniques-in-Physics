from matplotlib import pyplot as plt
import math as mt
import numpy as np
N=[2,20,200,500]
#Define axes and figures for the histograms
fig, ax = plt.subplots()
fig0, ax0 = plt.subplots()
for n in N:
   xmean=[]
   ymean=[]
   for i in range(10000):
       #Draw N samples from exponential distribution and find mean
       x=np.random.exponential(scale=0.5,size=n)
       xmean.append(np.mean(x))
       #Draw N samples from uniform distribution and find mean
       y=np.random.uniform(0.,4.,size=n)
       ymean.append(np.mean(y))
   #Calculate the std of the mean values
   xstd=np.std(xmean)
   ystd=np.std(ymean)
   #Draw histogram of mean values of x and y for each N
   ax.hist(xmean,100,label="N="+str(n)+", std="+str(round(xstd,2)))
   ax0.hist(ymean,100,label="N="+str(n)+", std="+str(round(ystd,2)))
ax.set_xlabel('Mean value of x')
ax.legend()
ax0.set_xlabel('Mean value of y')
ax0.legend()
plt.show()
