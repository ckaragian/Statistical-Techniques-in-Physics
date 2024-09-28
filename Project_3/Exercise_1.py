import math as mt
import numpy as np
from matplotlib import pyplot as plt

sigma=np.array([i+1 for i in range(20)])
x1=0.59*sigma
x2=1.91*sigma

plt.hlines(sigma,x1,x2)
plt.text(2, 1, '$\sigma$='+str(sigma[0]), ha ='left', va ='center')
plt.text(4, 2, '$\sigma$='+str(sigma[1]), ha ='left', va ='center')
plt.text(6, 3, '$\sigma$='+str(sigma[2]), ha ='left', va ='center')
plt.text(8, 4, '$\sigma$='+str(sigma[3]), ha ='left', va ='center')
plt.text(10, 5, '$\sigma$='+str(sigma[4]), ha ='left', va ='center')
plt.text(12, 6, '$\sigma$='+str(sigma[5]), ha ='left', va ='center')
plt.text(14, 7, '$\sigma$='+str(sigma[6]), ha ='left', va ='center')
plt.text(16, 8, '$\sigma$='+str(sigma[7]), ha ='left', va ='center')
plt.text(18, 9, '$\sigma$='+str(sigma[8]), ha ='left', va ='center')
plt.text(20, 10, '$\sigma$='+str(sigma[9]), ha ='left', va ='center')
plt.text(3, 11, '$\sigma$='+str(sigma[10]), ha ='left', va ='center')
plt.text(3.5, 12, '$\sigma$='+str(sigma[11]), ha ='left', va ='center')
plt.text(4, 13, '$\sigma$='+str(sigma[12]), ha ='left', va ='center')
plt.text(4.5, 14, '$\sigma$='+str(sigma[13]), ha ='left', va ='center')
plt.text(5, 15, '$\sigma$='+str(sigma[14]), ha ='left', va ='center')
plt.text(5.5, 16, '$\sigma$='+str(sigma[15]), ha ='left', va ='center')
plt.text(6, 17, '$\sigma$='+str(sigma[16]), ha ='left', va ='center')
plt.text(6.5, 18, '$\sigma$='+str(sigma[17]), ha ='left', va ='center')
plt.text(7, 19, '$\sigma$='+str(sigma[18]), ha ='left', va ='center')
plt.text(7.5, 20, '$\sigma$='+str(sigma[19]), ha ='left', va ='center')
plt.xlabel("x")
plt.ylabel("$\sigma$")
plt.title("Confidence belt")
plt.show()
