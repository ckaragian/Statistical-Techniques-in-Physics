from matplotlib import pyplot as plt
import math as mt
import numpy as np
import ROOT
from ROOT import gStyle
#Define figures and axes for the plots
fig,ax=plt.subplots()
fig1,ax1=plt.subplots()
N=[5,50,200,500]
mn=[]
stdn=[]
#Loop through all N
for n in N:
 I=[]
 #repeat for 10000 times
 for i in range(10000):
  #Draw uniform r in (0,1)
  r=np.random.uniform(0.,1.,n)
  #Draw uniform theta in (0,pi/2)
  theta=np.random.uniform(0.,mt.pi/2.,n)
  #Define the function integrated
  f=r**4*np.cos(theta)**2*np.sin(theta)
  #Calculate I_n
  I.append(mt.pi/2*np.mean(f))
 m=np.mean(I)
 mn.append(m)
  std=np.std(I)
 stdn.append(std)
 ax.hist(I,100,label="N="+str(n)+", mean="+str(round(m,4))+", std="+str(round(std,4)))
ax.set_xlabel('Distribution of I for different N')
ax.legend()
n=np.arange(len(N))
#Make a plot with mu_n and its std as error
ax1.scatter(N,mn, color = 'k')
ax1.errorbar(N,mn,yerr=stdn, ls="None", color = 'k')
#Plot the exact value of I
ax1.axhline(y = 1/15.,label="Exact value of I", color = 'r')
ax1.set_xlabel('N')
ax1.set_xlabel('Mean value of I')
ax1.legend()
plt.show()
#Calculate the ratio std/mean
dev=np.divide(stdn,mn)
#Plot this ratio as a function of N and fit a curve to it
canvas = ROOT.TCanvas()
canvas.cd(1)
N=np.array(N,dtype='d')#N and dev need to be of same dtype for TGraph
gr=ROOT.TGraph(4, N, dev)
gr.SetTitle("Relative deviation as a function of N; N; #sigma_{N}/#mu_{N}")
gr.SetMarkerColor(4)
gr.SetMarkerStyle(21)
gr.SetMarkerSize(2)
gr.Draw("AP")
#Define fit function
fit=ROOT.TF1("inverse root","[0]/sqrt(x)",0,600)
gr.Fit("inverse root","R")
#Create legend
leg=ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.AddEntry(fit,"1.70/#sqrt{N}","l")
leg.Draw("same")
canvas.Draw()
canvas.SaveAs("mcintegration.png")
#Get the fitted parameter
par=fit.GetParameters()
A=par[0]
#Print the results
print("The fitted constant A is: ", round(A,1))
print("The least amount of points so that we have deviation less than 1% is: ", mt.ceil(round(A,1)**2*10000))
