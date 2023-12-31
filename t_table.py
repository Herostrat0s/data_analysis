import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data1T=stats.t.rvs(loc=0,df=1,size=15)
data2T=stats.t.rvs(loc=0,df=2,size=15)

plt.xlim(-5,5)
sns.distplot(data1T,color="red",hist=False)
sns.distplot(data2T,color="blue",hist=False)
plt.show()
