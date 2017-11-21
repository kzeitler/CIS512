#Imported as example from https://stackoverflow.com/questions/22611446/perform-2-sample-t-test
import numpy as np
from scipy.stats import ttest_ind, ttest_ind_from_stats
from scipy.special import stdtr

np.random.seed(4)

# Create sample data.
a = np.random.randn(40)
b = np.random.randn(40)+3

print(a)
print(b)

# Use scipy.stats.ttest_ind.
t, p = ttest_ind(a, b, equal_var=False)
print("ttest_ind:            t = %g  p = %g" % (t, p))

#Get Average and stdev for a and b

avgA = np.mean(a)
print ("average for A" , avgA)

avgB = np.mean(b)
print ("average for B" , avgB)

stddevA = np.std(a=a)
stddevB = np.std(a=b)
print ("stddev for A:" , stddevA, "stddev for B:" , stddevB)

#Box and whisker plot
#Example from https://plot.ly/matplotlib/box-plots/
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.tools as tls

#combine data into a two-dimensional array
#data = [a,b]
#plt.boxplot(data)
#plt.show()

label = [i for i in range(1,40)]
print(label)
aplusb=[]
for i in label:
    aplusb.append(a[i]+b[i])

print(aplusb)

df = DataFrame(data=[a,b,aplusb],index=label)
df.cumsum()
plt.figure()

