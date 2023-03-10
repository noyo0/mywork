# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:53:57 2023

@author: norbe
"""

import csv

filename = "MOCK_DATA.csv"
domains = {}
with open(filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    firstline=True
    for line in csvReader:
        if firstline:
            firstline = False
            continue
        email = line[9]
        name = line[1]
        split = email.split("@")
        domain = split[1]
        if domain not in domains:
            domains[domain]=1
        else:
            domains[domain]+=1
                   
for key, value in domains.items():
    print(key,value)
        
        