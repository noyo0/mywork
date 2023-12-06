# w8lap.py
# Author: Norbert Antal

import numpy as np

minSal = 28000
maxSal = 88000
entries = 10
np.random.seed(1)
salaries = np.random.randint(minSal,maxSal,entries)
salariesPlus = salaries + 5000
PercentIncrease = (salaries*1.05).astype(int)

print(salaries)
print(salariesPlus)
print(PercentIncrease)