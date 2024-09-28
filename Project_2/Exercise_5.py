import numpy as np
import math as mt
from matplotlib import pyplot as plt
import ROOT

e=0.1

#Get uniform values for x
x=np.random.uniform(0,10,20)

#Get a random variable following the normal distribution with 0 mean and 1 std
w=np.random.normal(0,1,20)

#Get the value for y
y=-0.5*x+5+e*w

#Define the canvas for the graphs
canvas=ROOT.TCanvas()
canvas.cd(1)

#Define graph with (x,y)
gr=ROOT.TGraphErrors(20,x,y,np.zeros(20),e*np.ones(20))
gr.SetTitle("y=#mu+e*N(0,1)")
gr.SetMarkerColor(4)
gr.SetMarkerStyle(21)
gr.SetMarkerSize(2)
gr.Draw("AP")
#Define the linear fit function
fit=ROOT.TF1("linear","[0]+[1]*x",0,20)
#Define the quadratic fit function
fit1=ROOT.TF1("quadratic","[0]+[1]*x+[2]*x^2",0,20)
r=gr.Fit("linear","RS")
#Get the covariance matrix
cov=r.GetCovarianceMatrix()
#Get chi2 and Ndf
chi2=r.Chi2()
Ndf=r.Ndf()
#Create legend
leg=ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.AddEntry(fit,"a+b*x","l")
leg.Draw("same")
canvas.Draw()
canvas.SaveAs("linear.png")
r1=gr.Fit("quadratic", "RS")
#Get the covariance matrix
cov1=r1.GetCovarianceMatrix()
#Get chi2 and Ndf
chi21=r1.Chi2()
Ndf1=r1.Ndf()
#Create legend
leg=ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.AddEntry(fit1,"a+b*x+c*x^2","l")
leg.Draw("same")
canvas.Draw()
canvas.SaveAs("quadratic.png")
#Print the covariance matrices
cov.Print()
cov1.Print()
#Print the ratios chi2/ndf
print(chi2/Ndf,chi21/Ndf1)


#Define the lists to store the values for each iteration
a_list=[]
b_list=[]
sigmaa_list=[]
sigmab_list=[]
chi2_list=[]
p_value_list=[]

for i in range(1000):
   #Get uniform values for x
   x=np.random.uniform(0,10,20)

   #Get a random variable following the normal distribution with 0 mean and 1 std
   w=np.random.normal(0,1,20)

   #Get the value for y
   y=-0.5*x+5+e*w

   #Define graph with (x,y)
   gr=ROOT.TGraphErrors(20,x,y,np.zeros(20),e*np.ones(20))
   #Define the linear fit function
   fit=ROOT.TF1("linear","[0]+[1]*x",0,20)
   r=gr.Fit("linear","RS")
   #Get the covariance matrix
   cov=r.GetCovarianceMatrix()
   #Get chi2 and p-value and a and b parameters and put them in the lists
   chi2=r.Chi2()
   p_value=r.Prob()
   a=r.Parameter(0)
   sigmaa=mt.sqrt(cov[0,0])
   b=r.Parameter(1)
   sigmab=mt.sqrt(cov[1,1])
   a_list.append(a)
   b_list.append(b)
   sigmaa_list.append(sigmaa)
   sigmab_list.append(sigmab)
   chi2_list.append(chi2)
   p_value_list.append(p_value)

#Calculate the values to be plotted
z_a=(np.array(a_list)-5)/np.array(sigmaa_list)
z_b=(np.array(b_list)+0.5)/np.array(sigmab_list)

#Make the plots
plt.hist(a_list,100)
plt.xlabel("a")
plt.show()
plt.hist(b_list,100)
plt.xlabel("b")
plt.show()
plt.hist(z_a,100)
plt.xlabel("(a-$a_{true}$)/$\sigma_a$")
plt.show()
plt.hist(z_b,100)
plt.xlabel("(b-$b_{true}$)/$\sigma_b$")
plt.show()
plt.hist(chi2_list,100)
plt.xlabel("$\chi^2$")
plt.show()
plt.hist(p_value_list,100)
plt.xlabel("p-value")
plt.show()
