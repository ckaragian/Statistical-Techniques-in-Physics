import numpy as np
import math as mt
from matplotlib import pyplot as plt
from scipy.stats import norm, chi2
from scipy.optimize import curve_fit


# Define the Gaussian function 
def Gauss(x, a, x0, sigma): 
    return a/sigma/mt.sqrt(2*mt.pi)*np.exp(-(x-x0)**2/(2*sigma**2)) 

x=np.arange(-2.75,3.25,0.5)

pdf1=[0.0042, 0.0186, 0.0422, 0.0926, 0.1456, 0.1886, 0.1866, 0.1514, 0.0894, 0.0546, 0.0176, 0.0066]

pdf1err=[0.0009, 0.0019, 0.0029, 0.0043, 0.0054, 0.0061, 0.0061, 0.0055, 0.0042, 0.0033, 0.0019, 0.0011]

#Fit gauss curve to find the parameters for the chi2 test
parameters1, covariance1 = curve_fit(Gauss, x, pdf1)

print(parameters1)

pdf2=[0.0056, 0.0214, 0.0422, 0.0844, 0.1296, 0.1660, 0.1736, 0.1536, 0.1072, 0.0626, 0.0340, 0.0136]

pdf2err=[0.0011, 0.0021, 0.0029, 0.0041, 0.0051, 0.0058, 0.0059, 0.0055, 0.0046, 0.0035, 0.0026, 0.0016]

#Fit gauss curve to find the parameters for the chi2 test
parameters2, covariance2 = curve_fit(Gauss, x, pdf2)

print(parameters2)

plt.bar(x,pdf1,yerr=pdf1err,label="PDF1")
plt.scatter(x,pdf1)
plt.plot(x,parameters1[0]*norm.pdf(x,loc=parameters1[1],scale=parameters1[2]))
plt.legend()
plt.show()

plt.bar(x,pdf2,yerr=pdf2err,label="PDF2")
plt.scatter(x,pdf2)
plt.plot(x,parameters2[0]*norm.pdf(x,loc=parameters2[1],scale=parameters2[2]))
plt.legend()
plt.show()

#Calculate chi2 for the different datasets and compare with chi2 value for ndf=12-3 and a=0.1
Chi21=np.power((pdf1-parameters1[0]*norm.pdf(x,loc=parameters1[1],scale=parameters1[2])),2)/np.power(pdf1err,2)
Chi21=sum(Chi21)
print(Chi21)
print(chi2.ppf(1-0.1, df=9))

Chi22=np.power((pdf2-parameters2[0]*norm.pdf(x,loc=parameters2[1],scale=parameters2[2])),2)/np.power(pdf2err,2)
Chi22=sum(Chi22)
print(Chi22)
print(chi2.ppf(1-0.1, df=9))

#Calculate z value for the different datasets
N=[]
r=1
for i,y in enumerate(pdf1):
  #Calculate the difference of data and model
  diff=y-parameters1[0]*norm.pdf(x[i],loc=parameters1[1],scale=parameters1[2])
  #Count how many positive and negative differences there are and calculate the number of runs
  if diff>0:
    N.append(1)
    if N[i-1]==-1:
      r+=1
  else:
    N.append(-1)
    if N[i-1]==1:
      r+=1
print(r,N)

#Calculate N+ and N- and then E and V so that we get z
Nplus = sum(i for i in N if i > 0 )
Nminus=len(N)-Nplus
E=1+2*Nplus*Nminus/12
V=2*Nplus*Nminus*(2*Nplus*Nminus-12)/144/11
z=(r-E)/mt.sqrt(V)
print(z)
#Find p value of z
p_value=norm.sf(z)
print(p_value)

N=[]
r=1
for i,y in enumerate(pdf2):
  #Calculate the difference of data and model
  diff=y-parameters2[0]*norm.pdf(x[i],loc=parameters2[1],scale=parameters2[2])
  #Count how many positive and negative differences there are and calculate the number of runs
  if diff>0:
    N.append(1)
    if N[i-1]==-1:
      r+=1
  else:
    N.append(-1)
    if N[i-1]==1:
      r+=1
print(r,N)

#Calculate N+ and N- and then E and V so that we get z
Nplus = sum(i for i in N if i > 0 )
Nminus=len(N)-Nplus
E=1+2*Nplus*Nminus/12
V=2*Nplus*Nminus*(2*Nplus*Nminus-12)/144/11
z=(r-E)/mt.sqrt(V)
print(z)
#Find p value of z
p_value=norm.sf(z)
print(p_value)
