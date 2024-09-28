import math as mt
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2

x=np.random.poisson(6,20)
m=np.mean(x)
mup=0.5/20*chi2.ppf(0.84, 2*(20*m+1))
mlo=0.5/20*chi2.ppf(0.16, 40*m)
print(mup,mlo)
mup1=0.5*chi2.ppf(0.84, 2*(x[0]+1))
mlo1=0.5*chi2.ppf(0.16, 2*x[0])
print(mup1,mlo1)
