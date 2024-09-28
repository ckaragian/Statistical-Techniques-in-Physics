import math as mt
import numpy as np

#Define the lists with the uncertainties of each measurement
stat_unc=[8.,9.,2.,25.]
syst_unc=[27.,38.,27.,118.]
lumi_unc=[19.,19.,20.,23.]

#Calculate the statistical errors
V_stat=np.identity(4)

for i in range(4):
 V_stat[i,i]=stat_unc[i]**2

print(V_stat)

#Calculate the systematics
V_syst=np.ones((4,4))

for i in range(4):
 for j in range(4):
  if i==j:
   V_syst[i,j]=syst_unc[i]**2
  elif i==0 and j>0:
   V_syst[i,j]=0.2*syst_unc[i]*syst_unc[j]
  elif j==0 and i>0:
   V_syst[i,j]=0.2*syst_unc[i]*syst_unc[j]
  else:
   V_syst[i,j]=0.4*syst_unc[i]*syst_unc[j]

print(V_syst)

#Calculate the errors due to the luminosity
V_lumi=np.ones((4,4))

for i in range(4):
 for j in range(4):
  if i==j:
   V_lumi[i,j]=lumi_unc[i]**2
  elif i==0 and j>0:
   V_lumi[i,j]=0.9*lumi_unc[i]*lumi_unc[j]
  elif j==0 and i>0:
   V_lumi[i,j]=0.9*lumi_unc[i]*lumi_unc[j]
  else:
   V_lumi[i,j]=lumi_unc[i]*lumi_unc[j]

print(V_lumi)

#Calculate the total covariance matrix
V=V_stat+V_syst+V_lumi

print(V)

#Put measurements in a list
sigma=[818., 815., 888., 834.]

#Calculate the inverse covariance matrix
V_inv=np.linalg.inv(V)

u=np.ones(4)

norm=np.matmul(u.T,np.matmul(V_inv,u))

#Calculate w
w=np.matmul(V_inv,u)/norm

#Calculate the estimation for the cross section and its error
sigma_hat=np.matmul(w.T,sigma)

var=np.matmul(w.T,np.matmul(V,w))

#Print the values
print("σ=",round(sigma_hat,-1)," δσ=",round(mt.sqrt(var),-1))
