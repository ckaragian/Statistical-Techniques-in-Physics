import math as mt
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2, t

N=[5,20,50]

#Loop through different k=5,20,50
for n in N:
 #Produce samples of normal distribution
 x=np.random.normal(20,2,n)
 #Calculate it's mean and std
 mean=np.mean(x)
 std=np.std(x,ddof=1)
 #Calculate the lower and upper limit of the variance confidence interval
 varlo=(n-1)*std**2/chi2.ppf(0.95, n-1)
 varup=(n-1)*std**2/chi2.ppf(0.05, n-1)
 #Calculate the lower and upper limit of the mean confidence interval
 meanlo=mean-t.ppf(0.95, n-1)*std/mt.sqrt(n)
 meanup=mean+t.ppf(0.95, n-1)*std/mt.sqrt(n)
 
 print("For n=",n," there is 90% chance that the mean is >",meanlo," and <",meanup,".")
 print("For n=",n," there is 90% chance that the variance is >",varlo," and <",varup,".")


#Loop through different k=5,20,50
for n in N:
  a=[]
  b=[]
  counter1=0
  counter2=0
  #Iterate 1000 times for each k
  for i in range(1000):
    #Produce samples of normal distribution
    x=np.random.normal(20,2,n)

    #Calculate it's mean and std
    mean=np.mean(x)
    std=np.std(x,ddof=1)
 
    #Calculate the lower and upper limit of the variance confidence interval
    varlo=(n-1)*std**2/chi2.ppf(0.95, n-1)
    varup=(n-1)*std**2/chi2.ppf(0.05, n-1)
    
    #Calculate the lower and upper limit of the mean confidence interval
    meanlo=mean-t.ppf(0.95, n-1)*std/mt.sqrt(n)
    meanup=mean+t.ppf(0.95, n-1)*std/mt.sqrt(n)
    
    #Count how many intervals have the true parameter values
    if meanlo<=20 and meanup>=20:
     counter1+=1
    if varlo<=4 and varup>=4:
     counter2+=1
    
    #Fill the lists to make the histograms for questions a) and b)
    a.append(mt.sqrt(n)*(mean-20)/std)
    b.append((n-1)*std**2/4)
  
  #Make histograms
  plt.hist(a,100)
  plt.title("k="+str(n))
  plt.xlabel(r'$\sqrt{k}(\bar{x}-20)/s$')
  plt.show()
  plt.hist(b,100)
  plt.title("k="+str(n))
  plt.xlabel(r'$(k-1)s^2/4$')
  plt.show()
  print("For k=",n," ",counter1/1000," of the intervals have the exact mean value")
  print("For k=",n," ",counter2/1000," of the intervals have the exact variance value")
