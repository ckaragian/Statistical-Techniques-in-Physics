import numpy as np
import math as mt
from matplotlib import pyplot as plt
from scipy.stats import norm, uniform, chi2

#Produce samples from uniform and normal distribution
x1=np.random.uniform(0,1,100)

x2=np.random.normal(0,1,100)

#Produce datapoints for the plots
x_uniform=np.linspace(0,1,100)
x_normal=np.linspace(-2,2,100)

#Calculate the empirical cdf for each sample
cdf1=[]
for x in x_uniform:
 s=0
 for xi in x1:
  if xi<=x:
    s+=1
 cdf1.append(s/100)

cdf2=[]
for x in x_normal:
 s=0
 for xi in x2:
  if xi<=x:
    s+=1
 cdf2.append(s/100)

#Make the plots
plt.plot(x_uniform,cdf1,label="Empirical CDF")
plt.plot(x_uniform, uniform.cdf(x_uniform), color='k',label="Theoretical CDF")
plt.xlabel("x")
plt.title("Uniform Distribution")
plt.legend()
plt.show()
plt.plot(x_normal,cdf2,label="Empirical CDF")
plt.plot(x_normal, norm.cdf(x_normal), color='k',label="Theoretical CDF")
plt.xlabel("x")
plt.title("Normal Distribution")
plt.legend()
plt.show()

#Calculate the max absolute deviation
D_uniform=max(np.abs(cdf1-uniform.cdf(x_uniform)))
D_norm=max(np.abs(cdf2-norm.cdf(x_normal)))

print(D_uniform,D_norm)

D_uniform=[]
D_norm=[]
for i in range(10000):
 #Produce samples from uniform and normal distribution
 x1=np.random.uniform(0,1,100)

 x2=np.random.normal(0,1,100)
 
 x_uniform=np.linspace(0,1,100)
 x_normal=np.linspace(-2,2,100)
 
 #Calculate the empirical cdf for each sample
 cdf1=[]
 for x in x_uniform:
  s=0
  for xi in x1:
   if xi<=x:
     s+=1
  cdf1.append(s/100)

 cdf2=[]
 for x in x_normal:
  s=0
  for xi in x2:
   if xi<=x:
     s+=1
  cdf2.append(s/100)
 
 #Calculate the max absolute deviation
 D_uniform.append(mt.sqrt(100)*max(np.abs(cdf1-uniform.cdf(x_uniform))))
 D_norm.append(mt.sqrt(100)*max(np.abs(cdf2-norm.cdf(x_normal))))

#Make the histogram of the max absolute deviation
n1, bins1, patches1 = plt.hist(D_uniform,50)
plt.xlabel("$\sqrt{n}D$")
plt.title("Uniform Distribution")
plt.show()
n2, bins2, patches2 = plt.hist(D_norm,50)
plt.xlabel("$\sqrt{n}D$")
plt.title("Normal Distribution")
plt.show()

R=n1/10000
S=n2/10000
print(R)
print(S)

x=np.power(R-S,2)/(R+S)
x=x[~np.isnan(x)]

Chi2=sum(x)

print(Chi2)

k = np.count_nonzero(n1)

print(chi2.ppf(1-0.1,k-1))
