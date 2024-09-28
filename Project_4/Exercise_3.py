import numpy as np
import math as mt
from matplotlib import pyplot as plt
from scipy.stats import t,norm, f

x1mean=1.07
x2mean=1.18

n=100

s1=0.10

s2=0.12

ti=t.ppf(0.025,df=n-1)

t_value=(x1mean-x2mean)/(mt.sqrt((s1**2+s2**2)/n))

print(t_value,ti)

print(f.ppf(1-0.05,9,7))
print(f.ppf(0.05,9,7))

print(t.cdf(ti+0.11/(mt.sqrt((s1**2+s2**2)/n)),n-1))
