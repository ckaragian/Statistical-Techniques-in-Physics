from matplotlib import pyplot as plt
import math as mt
import numpy as np

#Define log-likelihood function
def lnL(s):
   x=[0.96, 1.12, 0.85, 1.02, 1.58, 1.86, 0.79, 0.82, 0.45, 1.52]
   ln=0
   for xi in x:
    ln+=np.log(xi/s**2)-xi**2/2/s**2
   return ln

sigma=np.linspace(0.5,1.5,10000)
lnL0=lnL(sigma)
#Calculate the maximum value of log-likelihood
lnLmax=lnL(0.81)-0.5
#Plot the log-likelihood
plt.scatter(sigma, lnL0, color = 'c', marker='x')
plt.plot(sigma, lnL0, color='k')
plt.axhline(y = lnLmax, label="lnL_{max}-0.5", color='r')
plt.axvline(x = 0.71,linestyle='--')
plt.axvline(x = 0.98,linestyle='--')
plt.axvline(x = 0.81,linestyle='--')
plt.xticks((0.71,0.81,0.98))
plt.xlabel('σ')
plt.ylabel('lnL')
plt.legend()
plt.show()

#Make plot with the parabolic approximation
plt.plot(sigma, lnL0, color='k')
sigmaapprox=np.linspace(0.6,1.0,100)
lnLapprox=lnL(0.81)-0.5/0.016*(sigmaapprox-0.81)**2
plt.plot(sigmaapprox, lnLapprox, color='g', linestyle='--',label='Parabolic approximation')
plt.xlabel('σ')
plt.ylabel('lnL')
plt.legend()
plt.show()
