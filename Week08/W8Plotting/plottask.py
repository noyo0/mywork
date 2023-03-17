# plottask.py
# Author: Norbert Antal
# Weekly Task 8
# Write a program called plottask.py that displays:
# a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x**3 in the range [0, 10], on the one set of axes.
# matplotlib ref: https://matplotlib.org/stable/tutorials/introductory/quick_start.html
# customise default style ref: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot


import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.normal(5,2,1000) # 1000 values with a mean of 5 and standard deviation of 2

# ------ h(x)=x**3--------------->
xcubed=[]
for i in range(0,11):
    x=i**3
    xcubed.append(x)
#---------------------------------I
#-----------def plot font styles------------------------------>
small = 8
med = 10
big = 14
plt.rc('font', size=small)          # controls default text sizes
plt.rc('axes', titlesize=small)     # fontsize of the axes title
plt.rc('axes', labelsize=med)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=small)    # fontsize of the tick labels
plt.rc('ytick', labelsize=small)    # fontsize of the tick labels
plt.rc('legend', fontsize=small)    # legend fontsize
plt.rc('figure', titlesize=big)  # fontsize of the figure title
plt.rc('font', family='serif')          # controls default text style
specfont1 = {'family':'serif','color':'brown','size':11}
specfont2 = {'family':'helvetica','color':'darkred','size':8}
#--------------------------------------------------------------I
#---------------labels---------------------->
plt.title("""Figure 1. - A histogram of a normal distribution 
of 1000 values with a mean of 5, and standard deviation of 2, 
and a plot of the function  h(x)=x^3 in the range [0, 10]""", fontdict=specfont1)
plt.xlabel("x axis",color="grey")
plt.ylabel("y axis", color="grey")
#-------------------------------------------I
#--------plot data ----------->
plt.hist(numbers,color='green')
plt.plot(xcubed,color="red")
#-----------------------------I
plt.legend(["x cubed","normal distribution"])
plt.show()