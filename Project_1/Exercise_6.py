from matplotlib import pyplot as plt
import math as mt
import numpy as np
from scipy.stats import multivariate_normal
import ROOT
#Define the probability density
def f(x):
    f=multivariate_normal(mean=[1,3], cov=[[1,-0.6],[-0.6,2]])
    return f.pdf(x)
#Define the autocorrelation function
def R(x,k,N):
  s1=0
  s2=0
  s3=0
  s4=0
  for i in range(N-k):
    s1+=(x[i,0]-np.mean(x[:,0]))*(x[i+k,0]-np.mean(x[:,0]))
    s2+=(x[i,0]-np.mean(x[:,0]))**2
    s3+=(x[i,1]-np.mean(x[:,1]))*(x[i+k,1]-np.mean(x[:,1]))
    s4+=(x[i,1]-np.mean(x[:,1]))**2
  return (s1+s3)/(s2+s4)
#Initialise x to (-5,-5)
x=-5*np.ones((10000,2))
#Lists for accepted points
xacc=[]
yacc=[]
rejected=0
accepted=0
for i in range(9999):
   x_next=np.random.multivariate_normal(mean=[x[i,0],x[i,1]], cov=0.3*np.identity(2))
   if np.random.random_sample() < min(1, f(x_next)/f(x[i])):
       x[i+1,0] = x_next[0]
       x[i+1,1] = x_next[1]
       xacc.append(x_next[0])
       yacc.append(x_next[1])
       accepted+=1;
   else:
       x[i+1,0] = x[i,0]
       x[i+1,1] = x[i,1]
       rejected+=1;
#Print accepted and rejected events
print("Number of accepted events = ",accepted)
print("Number of rejected events = ",rejected)
#Make a 2d histogram with all the 1000 generated events
canvas = ROOT.TCanvas()
canvas.cd(1)
#Fill the histogram with the values of x
th2f = ROOT.TH2F("Generated Events", "; x; y", 50, -5., 5., 50, -5., -5.)
for i in range(10000):
    th2f.Fill(x[i,0],x[i,1])
th2f.SetStats(0)
th2f.SetTitle("Generated Events")
th2f.Draw("ColZ")
canvas.Draw()
canvas.SaveAs("MHGenerated.png")
#Print the mean value of y and x their covariance matrix
print("Mean value of x for the generated events is: ", np.mean(x[:,0]))
print("Mean value of y for the generated events is: ", np.mean(x[:,1]))
print("Covariance matrix for the generated events is: \n", np.cov(x[:,0],x[:,1]))
#Make a 2d histogram with only the accepted events
canvas = ROOT.TCanvas()
canvas.cd(1)
#Fill the histogram with the values of x
th2f = ROOT.TH2F("Accepted Events", "; x; y", 50, -5., 5., 50, -5., -5.)
for i in range(len(xacc)):
    th2f.Fill(xacc[i],yacc[i])
th2f.SetStats(0)
th2f.SetTitle("Accepted Events")
th2f.Draw("ColZ")
canvas.Draw()
canvas.SaveAs("MHAccepted.png")
#Print the mean value of y and x their covariance matrix
print("Mean value of x for the accepted events is: ", np.mean(xacc))
print("Mean value of y for the accepted events is: ", np.mean(yacc))
print("Covariance matrix for the accepted events is: \n", np.cov(xacc,yacc))
#Plot the generated values of x and y in each step in order to estimate the burn-in value
N=np.arange(len(x[:,0]),dtype='i')
plt.plot(N,x[:,0], color='r')
plt.xlabel("n")
plt.ylabel("x value from each draw")
plt.axhline(y=1.0)
plt.show()
plt.plot(N,x[:,1], color='g')
plt.xlabel("n")
plt.ylabel("y value from each draw")
plt.axhline(y=2.0)
plt.show()
#Delete the first 1000 generated points
np.delete(x,[0,1000])
#Calculate the autocorrelation for different values of k and plot it
R=[R(x,k,9000) for k in range(0,9000,100)]
k=np.arange(0,9000,100)
plt.scatter(k,np.absolute(R))
plt.plot(k, np.absolute(R))
plt.xlabel("k")
plt.ylabel("R(k)")
plt.show()
#Lists for uncorrelated points
xunc=[]
yunc=[]
for i in range(0,9000,10):
   xunc.append(x[i,0])
   yunc.append(x[i,1])
canvas = ROOT.TCanvas()
canvas.cd(1)
#Fill the histogram with the values of x
th2f = ROOT.TH2F("Uncorrelated Events", "; x; y", 50, -5., 5., 50, -5., -5.)
for i in range(len(xunc)):
    th2f.Fill(xunc[i],yunc[i])
th2f.SetStats(0)
th2f.SetTitle("Uncorrelated Events")
th2f.Draw("ColZ")
canvas.Draw()
canvas.SaveAs("MHUncorrelated.png")
#Print the mean value of y and x their covariance matrix
print("Mean value of x for the uncorrelated events is: ", np.mean(xunc))
print("Mean value of y for the uncorrelated events is: ", np.mean(yunc))
print("Covariance matrix for the uncorrelated events is: \n", np.cov(xunc,yunc))
