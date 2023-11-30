from scipy.stats import norm

prob = 1-norm(loc=5.3,scale=1).cdf(4.5)
print(prob)