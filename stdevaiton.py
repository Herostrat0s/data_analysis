import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


np.random.seed(0)
data = np.random.normal(35,2,40000)
zdata=stats.zscore(data)
sns.displot(zdata,kde=True)
plt.title("Data Distribution Table",fontsize=15,loc="right",c="red")
plt.xlabel("Data",fontsize=15,c="red")
plt.ylabel("Frequency",fontsize=15,c="red")
plt.axvline(x=np.mean(zdata),linestyle="--",linewidth=2.5,label="Mean",c="orange")
plt.axvline(x=np.mean(zdata)-np.std(data),linestyle="--",linewidth=2.5,label="Std",c="black")
plt.axvline(x=np.mean(zdata)+np.std(data),linestyle="--",linewidth=2.5,c="black")
plt.axvline(x=np.mean(zdata)-2*np.std(data),linestyle="--",linewidth=2.5,label="2 Std",c="blue")
plt.axvline(x=np.mean(zdata)+2*np.std(data),linestyle="--",linewidth=2.5,c="blue")
plt.legend()
plt.show()
