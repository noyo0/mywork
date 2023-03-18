# plottask_seaborn.py
# Author: Norbert Antal
# tutorial 1: https://www.youtube.com/watch?v=ooqXQ37XHMM
# tutorial 2: https://www.youtube.com/watch?v=6GUZXDef2U0


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#-----mydata-------------------
numbers = np.random.normal(5,2,1000) # 1000 values with a mean of 5 and standard deviation of 2
# ------ h(x)=x**3--------------->
xcubed=[]
for i in range(0,11):
    x=i**3
    xcubed.append(x)
#---------------------------------I
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
planets = sns.load_dataset("planets")

#sns.scatterplot(x="tip", y="total_bill", data=tips,hue="day", size="size", palette="coolwarm")

sns.histplot(numbers,kde=True, bins=150, color="green")
plt.show()