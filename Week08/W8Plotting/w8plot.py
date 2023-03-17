import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

minSal = 28000
maxSal = 88000
entries = 10
np.random.seed(1)
salaries = np.random.randint(minSal,maxSal,entries)
ages = np.random.randint(21,65,entries)
salariesPlus = salaries + 5000
PercentIncrease = (salaries*1.05).astype(int)
plt.scatter(ages, salaries)
plt.legend("€")
xp=np.array(range(1,101))
yp=xp*xp
plt.plot(xp,yp,color='green', label="x Sqr")
plt.title("random plt")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.show()
#plt.savefig('randomplot.png')
