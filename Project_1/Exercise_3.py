from matplotlib import pyplot as plt
import math as mt
import numpy as np
import ROOT
#We produce 1000 (pseudo)random numbers in [0,1) using random.rand() function of numpy
y=np.random.rand(1000)
#We produce 1000 random numbers of weibull distribution
x=np.sqrt(np.log(1/(1-y)))
#Calculate the first 4 moments
m=[]
for i in range(4):
    m.append(np.mean(x**i))
print(m)
#Plot the density function
#Define the graph for f(x)
x2=np.linspace(0,2.5,100)
f=2*x2*np.exp(-x2*x2)*20 #We multiply by 20 for visual purposes to scale up f(x) since it takes values from 0 to 1 and we have on average 20 counts per bin.
gr=ROOT.TGraph(100,x2,f)
canvas = ROOT.TCanvas()
canvas.cd(1)
#Fill the histogram with the values of x
th1f = ROOT.TH1F("Weibull_Distribution", "; x; Counts", 100, 0., 2.5)
for i in range(len(x)):
    th1f.Fill(x[i])
th1f.SetStats(0)
th1f.Draw()
gr.SetLineWidth(4)
gr.Draw("same")
#Create legend
leg=ROOT.TLegend(0.5,0.7,0.9,0.9)
leg.AddEntry(gr,"20f(x)=20(2xe^{-x^{2}})","l")
leg.Draw("same")
canvas.Draw()
canvas.SaveAs("weibull.png")
