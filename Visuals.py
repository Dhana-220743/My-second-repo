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
plt.show()'''
data = {
    'marks':[80,80,50,55,65,65,65,70,42,90,90,100]
}
df = pd.DataFrame(data)
df['name']= ['dhana','dhanu','raj','dhana','raj','raj','raj','dhana','dhanu','harsh','harsh','me']
df['age'] = [18,24,15,20,23,20,12,20,13,14,15,21]
print(df.head())
plt.scatter(df['marks'],df['age'],color = "pink")
plt.show()