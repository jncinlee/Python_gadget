##3 Matplotlib plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x+1
y = x**2
plt.plot(x,y)
plt.show()



##4 figure
#show in other window
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure(figsize=(5,8)) #in first fig
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5)) #in third fig
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=10,linestyle='--')

plt.show()



##5 axis, more than one plot in one figure
