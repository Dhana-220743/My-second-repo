import matplotlib.pyplot as plt
import pandas as pd
'''x={
    'marks':[89,45,34,76,21]
}
df = pd.DataFrame(x)
print(df)
plt.plot(df['marks'],color='red',marker = 'd',linestyle = 'dotted')
plt.grid()
plt.show()

data = {
    'marks':[80,80,50,55,65,65,65,70,42,90,90,100]
}
df = pd.DataFrame(data)
plt.hist(df['marks'],bins=3,color='blue')
plt.show()

x={
    'marks':[89,45,34,76,21]
}
df = pd.DataFrame(x)
df.loc[10] = 0
plt.boxplot(df['marks'])
plt.show()

data = {
    'marks':[80,80,50,55,65,65,65,70,42,90,90,100]
}
df = pd.DataFrame(data)
df['name']= ['dhana','dhanu','raj','dhana','raj','raj','raj','dhana','dhanu','harsh','harsh','me']
print(df.head())
count = df['name'].value_counts()
print(count)
plt.pie(count,labels= count.index , autopct = '%1.0f' , explode = [0,0,1,0,2])
plt.show()

plt.bar(count.index,count)
plt.show()
data = {
    'marks':[80,80,50,55,65,65,65,70,42,90,90,100]
}
df = pd.DataFrame(data)
df['name']= ['dhana','dhanu','raj','dhana','raj','raj','raj','dhana','dhanu','harsh','harsh','me']
df['age'] = [18,24,15,20,23,20,12,20,13,14,15,21]
print(df.head())
plt.scatter(df['marks'],df['age'],color = "pink")
plt.show()

import plotly.express as px
data = {
    'year':[2015,2016,2017,2018,2019],
    'sales':[100,150,200,180,250]
}
df = pd.DataFrame(data)
fig  = px.area(df,x='year',y='sales')
fig.show()
x = [0, 2, 4, 6, 8]
y = [0, 4, 16, 36, 64]
fig, ax = plt.subplots()
ax.plot(x, y, marker='o', label="Data Points")
ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
plt.show()'''

from pywaffle import Waffle
# Data representing market share
data = {'Company A': 30, 'Company B': 20, 'Company C': 50}
# Plotting the waffle chart
plt.figure( FigureClass=Waffle, rows=10, values=data,
colors=["#f94144", "#f3722c", "#90be6d"], legend={'loc':
'upper left', 'bbox_to_anchor': (1, 1)}, icons='star',
icon_size=20)
plt.title('Market Share of Companies')
plt.show()