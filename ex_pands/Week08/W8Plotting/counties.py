# Pie plot demo with counties
# Author: Norbert Antal

import numpy as np
import matplotlib.pyplot as plt

poscounties=["Wexford","Waterford","Cork","Dublin","Wicklow"]

counties=np.random.choice(poscounties,100,p=[0.1, 0.3, 0.2, 0.12, 0.28,])

print(counties)
unique, counts = np.unique(counties, return_counts=True)
plt.bar(unique,counts)
plt.legend()
plt.show()