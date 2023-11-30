import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(25,1,10000)
sns.displot(x,kde=True)
plt.show()