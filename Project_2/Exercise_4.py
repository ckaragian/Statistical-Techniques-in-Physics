import math as mt
import numpy as np
from matplotlib import pyplot as plt

#Define lny and t and the weights
lny=[4.24, 3.71, 3.79, 3.32, 2.84, 2.51, 2.05, 1.77, 1.97, 1.36]

t=[1,2,3,4,5,6,7,8,9,10]

weights=[25,25,25,25,25,25,25,25,27.7,22.7] 

#Compute the covariance matrix
cov=np.cov(t, lny, aweights=weights)

#Print the value of τ
print(-cov[0,0]/cov[0,1])

#Compute the logarithm of y_0
ln_y0=np.average(lny,weights=weights)-cov[0,1]/cov[0,0]*np.average(t,weights=weights)

#Print y_0
print(mt.exp(ln_y0))

#Calculate error of τ
dlny_0=mt.sqrt(np.average(np.power(t,2),weights=weights)/(np.average(np.power(t,2),weights=weights)-np.average(t,weights=weights)**2))/mt.sqrt(np.sum(weights))

#Calculate error of y_0
dy_0=mt.exp(ln_y0)*dlny_0

print(dy_0)

#Calculate error of lny_0
db=mt.sqrt(1/(np.average(np.power(t,2),weights=weights)-np.average(t,weights=weights)**2))/mt.sqrt(np.sum(weights))

dt=(cov[0,0]/cov[0,1])**2*db

print(dt)

#Calculate the correlation

r=-np.average(t,weights=weights)/mt.sqrt(np.average(np.power(t,2)))

print(r)
#Define the datapoints y and their errors sigmay
t=[1,2,3,4,5,6,7,8,9,10]
y=[69.4, 40.8, 44.4, 27.7, 17.1, 12.3, 7.8, 5.9, 7.2, 3.9]
sigmay=[13.9, 8.2, 8.9, 5.5, 3.4, 2.5, 1.6, 1.2, 1.4, 0.8]

#Define 100 points for which to calculate the curves for 1,0,-1 σ
tt=np.linspace(1,10,100)
yy=90*np.exp(-tt/3.17)
#Calculate the sigma for these points
dy=np.sqrt((yy*dt*tt*cov[0,1]**2/cov[0,0]**2)**2+(yy*dy_0/mt.exp(ln_y0))**2+r*dt*dy_0*yy*yy*tt/mt.exp(ln_y0)*cov[0,1]**2/cov[0,0]**2)

#Plot the datapoints with errorbars
plt.errorbar(t,y, yerr=sigmay, fmt="o", label="Data", color='g')
#Plot the curve with the mean values of y
plt.plot(tt,yy, label="Mean curve")
#Plot the +1σ curve
plt.plot(tt,yy+dy, label="1σ",color='r')
#Plot the -1σ curve
plt.plot(tt,yy-dy, color='r')
plt.xlabel("t(min)")
plt.ylabel("y")
plt.legend()
plt.show()
