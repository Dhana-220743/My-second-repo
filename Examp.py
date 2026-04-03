import pandas as pd
import numpy as np

'''mydata = {
    "Name":["Dhana","Lakshmi","Raju"],
    "Age" : [19,np.nan,24]
}
df = pd.DataFrame(mydata)
print(df)
#missing values
print(df.isnull())
print(df.isnull().sum())
print(df.notnull())
print(df["Age"].notnull())
print(df["Age"].fillna(method="pad"))
print(df.fillna(method='bfill'))
#filling values
print(df["Age"].fillna(21,inplace=False))
print(df["Age"].interpolate(method="linear"))
print(df.replace(np.nan,99,inplace=False))
print(df.dropna(axis=1,inplace=False))
print(df["Age"].fillna(21,inplace=True))
print(df.groupby('Name')['Age'].mean())
# Creating the dataset
data = {'Product': ['Laptop', 'Phone', 'Shirt', 'Jeans', 'Headphones', 'Jacket'],
        'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Clothing'],
        'Sales': [1000, 800, 50, 60, 200, 90]}
df = pd.DataFrame(data)
# Group by Category and sum Sales
grouped_data = df.groupby('Category')['Sales'].sum()
print(df)
print(grouped_data)
Grouping Employees by Department
•	📌 Problem: A company wants to know the average salary for each department.
•	Dataset:
Employee	Department	Salary ($)
Alice	HR	5000
Bob	IT	7000
Charlie	IT	8000
David	HR	5500
Eve	Sales	6000
data ={
    "Employee":["Alice","Bob","Charlie","David","Eve"],
    "Department":["HR","IT","IT","HR","Sales"],
    "Salary":[5000,7000,8000,5500,6000]
}
df=pd.DataFrame(data)
print(df)
print(df.groupby('Department')['Salary'].mean())
Large Dataset
Generate 100 random numbers between 10 and 100 and bin them into 10 equal-width bins.
data = np.random.randint(10,100,size=100)
print(data)
bins = pd.cut(data,bins=10)
print(bins)
bins = pd.qcut(data,q=10)
print(bins)'''
 
# Define the dataset
x = np.array([1,3,5,7,8,9, 10, 15])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80])
def Pearson_correlation(X,Y) :
    Sum_xy = sum((X -X.mean())*(Y-Y.mean()))
    Sum_xsq =sum((X-X.mean())**2)
    Sum_ysq = sum((Y-Y.mean())**2)
    cor = Sum_xy/np.sqrt(Sum_xsq * Sum_ysq)
    return cor

print("Correlation coefficient is:",Pearson_correlation(x,y))