# Project_2023.py
# Author: Norbert Antal
# pandas documentation: https://pandas.pydata.org/pandas-docs/stable/
# pandas tutorial ref: https://www.youtube.com/watch?v=vmEHCJofslg&t=111s
# matplotlib tutorial ref: https://www.youtube.com/watch?v=DAQNHzOcO5A
# matplotlib with pandas ref: https://www.youtube.com/watch?v=0P7QnIQDBJY
# add headers ref: https://www.geeksforgeeks.org/how-to-add-header-row-to-a-pandas-dataframe/
# Linear Discriminant Analysis1 https://www.youtube.com/watch?v=azXCzI57Yfc
# Linear Discriminant Analysis2 https://www.youtube.com/watch?v=9IDXYHhAfGA
# Principal Component Analysis


#########analysis ideas: ################################################
# - mean, standard dev plots
# - ranks> longest/shortest petal, longest/shortest sepal etc. in general and per 'class'
# - https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
# - https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset
# - https://www.analyticsvidhya.com/blog/2022/06/iris-flowers-classification-using-machine-learning/
# - holymoly wtf is this: https://commons.wikimedia.org/wiki/File:Principal_tree_for_Iris_data_set.png
# - pretty: https://knausb.github.io/morphometrics/ea_iris.html
# - typical petal/sepal sizes, intersections in sizes (what sizes can clearly distinguish the different species)
# -----> nice example: https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda#:~:text=Data%20Insights%3A,-The%20pdf%20curve&text=If%20petal%20length%20%3C%202.1%2C%20then,then%20species%20is%20Iris%20Virginica
# -----> very nice example https://www.kaggle.com/code/necibecan/iris-dataset-eda-n
# ----> BEST SOURCE!! - historsy of the Fisher's Iris data set: http://www.dicook.org/files/jsm19/slides#1 
# - dataset origins: https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.
# - CAN WE PROVE VERSICOLOR IS A HYBRID?
##########################################################################


"""headers:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#-------------------read in --------------------------------------------------------------------------------
file="iris.data"
#----read in with giving headers to each column-----------------------
df=pd.read_csv(file, names=[
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)",
    "class"])
#------------------------check first 5 lines-------------------------------------------------------
# print(df.head(5))

#____________________________---F I L T E R ---_________________________________________________________

print(df["class"]) #print "class" column only
#print(df["class"][145]) 145th entry in "class" column

#.............conditional filtering....__df.loc function____......................................
# # print(df.loc[df["petal length (cm)"]>6.1]) # conditional filtering
# ------------------combined filters-------------------
# print(df.loc[(df["class"] == "Iris-setosa") | (df["petal width (cm)"] == 0.2) & (df["sepal width (cm)"] > 3.2)]) # ----- "&" means AND, "|" means OR
# ---------------filter for part of text----------------------------------
# print(df.loc[df["class"].str.contains("setos")])
# ---------------filter OUT for part of text----------------------------------
#print(df.loc[~df["class"].str.contains("setos")]) 
#__________________________

#------------loop through individual objects---------------------------------------------------------------------------------------
#for index, row in df.iterrows(): # print individually each object
#    print(index, row['class']) #filter to 'class' column

#----------basic statistical-------------------------------------------------------------------------------------------
#print(df.describe()) # gives simple stats of the data.

#-----------basic plotting-------------------------------------------------------------------------------------------
# df.describe().plot(kind="bar") #plots a bar chjart of stats
# plt.show()
#stats = df.describe()
#stats.loc[stats.index != "count"].plot(kind="bar")   #----> plots bar chart without 'counbt' element
#plt.show()

#---------------SORTING -----------------------------------------------------------------------------------------------
#print(df.sort_values(["class","petal width  (cm)"], ascending=[1,0])) # class is ascending, petal widht is descending

#--****------making chnages to data------*****--------------------------------------

#------- add summary column "Total"----------------
#df['Total'] = df["sepal length (cm)"]+df["sepal width (cm)"]+df["petal length (cm)"]+df["petal width (cm)"]
#print(df.head(5))

#--------- remove column "Total" -----------------
#-------------another adding techinc (quicker)-----df.iloc[all rows, columns 1-3].sum˛[axis=0 rows, axis=1 columns]--
#df["Total"] = df.iloc[:,0:4].sum(axis='columns') # ----(axis=0 (or axis='rows' is horizontal axis. axis=1 (or axis='columns') is vertical axis)-----
#print(df.head(5))

#-----------Saving data --------------------------------
#df.to_csv("modified.csv")
#df.to_excel("modified_tab.xlsx", index=False) # save to Excle without 'index' column.
#df.to_csv("modified_tab.csv", index=False, sep='\t') # save to csv without 'index' column and tab separated not comma.