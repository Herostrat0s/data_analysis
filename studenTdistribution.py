import numpy as np
from scipy import stats
import matplotlib.py as plt
import seaborn as sns

np.random.seed(0)

dataT= stats.t.rvs(loc=0,df=1,size=15)
plt.xlim(-5,5)
sns.distplot(dataT,c="red")

