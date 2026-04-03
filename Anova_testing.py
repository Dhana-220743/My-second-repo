''' A teacher wants to check whether three different teaching methods produce different student
scores.
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = {
    "Method A": [78, 82, 85, 80],
    "Method B": [85, 88, 90, 87],
    "Method C": [92, 95, 89, 94]
}

df = pd.DataFrame(data)
print("Data:")
print(df)
group_means= df.mean()
total_mean= df.values.flatten().mean()

ssq = ((df - total_mean) ** 2).sum().sum()
n = df.size
ssb = sum(n * (group_means - total_mean) ** 2)
ssw = ssq - ssb

df_between = len(df.columns) - 1
df_within = n - len(df.columns)

msb = ssb / df_between
msw = ssw / df_within
f_statistic = msb / msw
print("F-statistic:", f_statistic)

2)Slightly larger datasets
import numpy as np
from scipy import stats

# Data
light1 = np.array([15,17,16,18])
light2 = np.array([18,16,19,17])
light3 = np.array([14,13,15,12])
light4 = np.array([20,22,21,23])

# Perform One-Way ANOVA
f_value, p_value = stats.f_oneway(light1, light2, light3, light4)

print("F-value:", f_value)
print("P-value:", p_value)



# Dataset
data = {
    'Yield': [30,32,31,40,42,41,28,29,27,38,37,39],
    'Fertilizer': ['A','A','A','A','A','A','B','B','B','B','B','B'],
    'Water': ['Low','Low','Low','High','High','High','Low','Low','Low','High','High','High']
}

df = pd.DataFrame(data)

# Model
model = ols('Yield ~ C(Fertilizer) + C(Water) + C(Fertilizer):C(Water)', data=df).fit()

# ANOVA Table
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

from scipy import stats
#4
A = [23, 20, 22, 21]
B = [30, 28, 27, 29]
C = [35, 33, 34, 36]

f_statistic, p_value = stats.f_oneway(A, B, C)

print("F-statistic:", f_statistic)
print("p-value:", p_value)'''

# 5 
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as ols
data = {
    'Diet':['A','A','A','B','B','B','C','C','C'],
    'Weight_loss':[5,6,4,8,7,9,3,2,4]
}
df = pd.DataFrame(data)
print("Data:",df)
#fit ANOVA model
model = ols('Weight_loss ~ C(Diet)', data=df).fit()
anova_table = sm.stats.anova_lm(model,typ=2)
print(anova_table)