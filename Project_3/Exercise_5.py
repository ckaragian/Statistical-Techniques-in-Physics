import math as mt
import numpy as np
from scipy.stats import f, norm

n=200

x=130

p=x/n

#Clopper-Pearson intervals
p1=x*f.ppf(0.16, 2*x, 2*(n-x+1))/(n-x+1+x*f.ppf(0.16, 2*x, 2*(n-x+1)))

p2=(x+1)*f.ppf(0.84, 2*(x+1), 2*(n-x))/(n-x+(x+1)*f.ppf(0.84, 2*(x+1), 2*(n-x)))

print("The C-P intervals for CL=0.68 are p1=",p1,"and p2=", p2)

#Wilson intervals
p1=(p+norm.ppf(0.84)**2/2/n)/(1+norm.ppf(0.84)**2/n)-norm.ppf(0.84)/(1+norm.ppf(0.84)**2/n)*mt.sqrt(p*(1-p)/n+norm.ppf(0.84)**2/4/n**2)

p2=(p+norm.ppf(0.84)**2/2/n)/(1+norm.ppf(0.84)**2/n)+norm.ppf(0.84)/(1+norm.ppf(0.84)**2/n)*mt.sqrt(p*(1-p)/n+norm.ppf(0.84)**2/4/n**2)

print("The Wilson intervals for CL=0.68 are p1=",p1,"and p2=", p2)
