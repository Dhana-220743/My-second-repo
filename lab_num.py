import numpy as np
import pandas as pd
import random 

# 1)Create a dataframe from numppy array with custom column names
a = np.array([['dairy_milk',40,20],['five_star',10,5],['milky_bar',100,50],['kitkat',50,25],['perk',20,10]])
df = pd.DataFrame(a,columns=['product_name','price','quantity'])
print(df)

# 2)Calculate the cumulative sum of a Numpy array and store the results in a new pandas dataframe column
df['quantity']=df['quantity'].astype(int)
df['cumulative_sum']=np.cumsum(df['quantity'])
print(df)

#3)Perform matrix multiplication using Numpy
m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.array([[[1,2],[3,4],[5,6]]])
print('Multiplying two matrices\n',np.matmul(m1,m2))

#4)Create a Numpy array with random values and find the unique values
arr = np.random.randint(0,10,5)
print(np.unique(arr))

#5)Create a new dataframe by transposing an existing values
a = np.array([['dairy_milk',40,20],['five_star',10,5],['milky_bar',100,50],['kitkat',50,25],['perk',20,10]])
df = pd.DataFrame(a,columns=['product_name','price','quantity'])
print('Original array:',df)
df_transpose = df.T
print('Transposed array',df_transpose)

#6)Write a Numpy program to create a 3*3 matrix with values ranging from 2 to 10 
m1 = np.arange(2,11)
m2 = m1.reshape((3,3))
print(m2)

#7)Write a Numpy program to Create a null vector with of size 10 update with sixth value
arr = np.zeros(10)
print('Before updating',arr)
arr[6] = 11
print('After updating\n',arr)

#8)Write a numpy program to create an array with values ranging from 12 to 38
arr = np.arange(12,38)
print(arr)

#9)Write a numpy program to find common values between two arrays
arr1 = np.array([10,13,45,60])
arr2 = np.array([13,66,90])
print(np.intersect1d(arr1,arr2))

#10)Write a numpy program to find set difference between two arrays .The set difference
    #will return sorted,distinct values in arr1 that are not in arr2
arr1 = np.array([10,13,95,60])
arr2 = np.array([13,66,90])
result = np.setdiff1d(arr1,arr2)
result.sort()
print(result)

#11)Write a Numpy program to compare two arrays using Numpy
arr1 = np.array([1,3])
arr2 = np.array([5,2])
print(f'{arr1} > {arr2} ')
print(arr1>arr2,'\n')
print(f'{arr1} < {arr2} ')
print(arr1<arr2,'\n')
print(f'{arr1} >= {arr2} ')
print(arr1>=arr2,'\n')
print(f'{arr1} <= {arr2} ')
print(arr1<=arr2,'\n')

#12)Write a Numpy program to create a 3-D array with ones on a diagonal and zeros elsewhere
arr = np.ones((3,3))
np.fill_diagonal(arr,0)
print(arr)

#13)Write a Numpy program to find the 4th element of a specified array
m1 = np.array([[1,2,3],[4,5,6]])
fourth_element = m1.flatten()[3]
print('forth element :',fourth_element)

#14)Write a Numpy program to convert 1-D arrays columns into a 2-D array
arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])
res = np.column_stack((arr1,arr2))
print(res)

#15)Write a Numpy program to create an array of (3,4) shapes,multiplies every element value by 3 and display this result
arr = np.arange(0,12)
arr1 =arr.reshape((3,4))
arr2 = np.dot(arr1,3)
print('multiply with 3',arr2)