from matplotlib import pyplot as plt
import math as mt
import numpy as np
def f(x):
   return 1-mt.comb(x, 3)*(0.6)**3*(0.4)**(x-3)-mt.comb(x, 2)*(0.6)**2*(0.4)**(x-2)-mt.comb(x, 1)*(0.6)*(0.4)**(x-1)-(0.4)**(x)
N=[i+4 for i in range(11)]
P=[f(i+4) for i in range(11)]
plt.bar(N, P, color = 'c', edgecolor = 'k')
plt.axhline(y = 0.95,label="95%")
plt.xticks(N)
plt.xlabel('Number of detectors')
plt.ylabel('Probability of detection')
plt.legend()
plt.show()
