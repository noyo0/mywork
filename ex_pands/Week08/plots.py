# practice with plotting using matplotlib
# Author: Norbert Antal

import numpy as np
import matplotlib.pyplot as plt

'''x=np.array(range(1,101))
y=x*x

plt.plot(x,y, label="x sqrd")
plt.plot(x,x,label="straight")
plt.legend()

randpoints = np.random.randint(1,1000,100)
plt.bar(x,randpoints,label="straight", color="red")

plt.show()
#plt.savefig("lect1.jpg")'''
#---------------------------
"""normdata= np.random.normal(size=10000)
plt.scatter(normdata)
plt.show()"""
#-----------------
fruit = np.array(['barack', 'korte', 'szilva','torkoly'])
numbers = np.array([55,49,66,68])
plt.pie(numbers, labels= fruit)
plt.legend()
plt.show()