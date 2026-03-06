import pandas as pd
# 1) DataSet 1 : Student Performance
data = {
    'Name':['Asha','Ravi','Kiran','Meena','John','Priya'],
    'Age':[20,21,None,22,20,None],
    'Marks':[85,None,78,90,None,88],
    'City':['Hyderabad','Chennai',None,'Mumbai','Delhi','Hyderabad']
}
df = pd.DataFrame(data)
print("Given data :\n",df)
# 1) Identify the missing values
print("Missing values\n")
print(df.isnull())
# 2) Count missing values column wise
print(df.isnull().sum())
# 3) Fill missing age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df['Age'])
# 4) Fill missing marks with median
df['Marks'] = df['Marks'].fillna(df['Marks'].median())
print(df['Marks'])
# 5) Fill missing City with mode
df['City'] = df['City'].fillna(df['City'].mode()[0])
print(df['City'])
# 6) Drop rows where marks are missing
df['Marks'] = df['Marks'].dropna()
# 7) Compare dataset before and after cleaning
print(df)

# 2) DataSet 2: Employee Records
data = {
    'Emp_ID':[101,102,103,101,104,105,102],
    'Name':['Ravi','Asha','John','Ravi','Kiran','Meena','Asha'],
    'Salary':[50000,60000,55000,50000,52000,58000,60000]
}
df = pd.DataFrame(data)
print("Original Data :\n",df)
# 1) Find duplicate rows
dup = df[df.duplicated()]
print(dup)
# 2) Remove duplicates
print(df.drop_duplicates())
# 3) Keep only first occurrence
df_clean= df.drop_duplicates(keep='first')
print(df_clean)
# 4) Check number of rows before and after removal
print("\n Rows before removing duplicates:",len(df))
print("Rows after removing duplicates :",len(df_clean))

# 3. Data Type conversion
data = {
    'Product':['A','B','C','D'],
    'Price':['100','200','150','300'],
    'Date':['01-01-2024','02-01-2024','03-01-2024','04-01-2024']
}
df = pd.DataFrame(data)
print("Original Data :\n",df)
print(df.dtypes)
# 1) Convert price to numeric
df['Price']=pd.to_numeric(df['Price'])
print(df['Price'])
# 2) Convert Date to Datetime
df['Date'] = pd.to_datetime(df['Date'],format='%d-%m-%Y')
print(df['Date'])
# 3) Check data types before and after conversion
print(df.dtypes)

# 4. Outlier Detection and Removal
Sales = [100,120,130,115,5000,140,125,110]
df = pd.DataFrame(Sales,columns=['Sales'])
# 1) Detect outlier using IQR method
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 -Q1
l_limit = Q1 - 1.5 * IQR
u_limit = Q3 + 1.5 * IQR
print("Lower limit :",l_limit)
print("Upper limit:",u_limit)

# identify the outlier
outliers = df[(df['Sales'] < l_limit) | (df['Sales'] > u_limit)]
print("Outliers :")
print(outliers)

# Remove outliers
df_clean = df[(df['Sales'] >= l_limit) & (df['Sales'] <= u_limit)]
print("Dataset After removing Outliers:",df_clean)

# compare Mean Before and After 
mean_before = df['Sales'].mean()
mean_after = df_clean['Sales'].mean()
print("Mean before Removing outlier :",mean_before)
print("Mean After Removing outlier :",mean_after)

# 5.Standardization and Normalization
import numpy as np
marks = np.array([50,60,70,80,90])
# 1) perform Min-Max normalization
min_val = np.min(marks)
max_val = np.max(marks)
normalized_marks = (marks - min_val) / (max_val - min_val)
print("Min-Max Normalized Marks:",normalized_marks)
# 2) Perform Z score Standardization
mean = np.mean(marks)
std = np.std(marks)
standardized_marks = (marks - mean) / std
print("Z-score Standardized Marks:",standardized_marks)
# 3) Compare both methods
print("Min-Max Normalization:",normalized_marks)
print("Z-score Standardization:",standardized_marks)

# 6. String cleaning
data = {
    'Email':[' test@gmail.com','RAVI@GMAIL.COM','john123 @gmail.com',None]
}
df = pd.DataFrame(data)
print("Original Data :\n",df)
# 1) Remove extra spaces
df['Email'] = df['Email'].str.strip()
print(df['Email'])
# 2) Convert to lowercase
df['Email'] = df['Email'].str.lower()
print(df['Email'])
# 3) Remove invalid spaces within email
df['Email'] = df['Email'].str.replace(r'\s+', '', regex=True)
print(df['Email'])
# 4) handle missing values
df['Email'] = df['Email'].fillna('No Email Provided')
print(df['Email'])
print(df)

# 7. Binning
ages = [18,22,25,30,35,40,45,50]
df = pd.DataFrame(ages, columns=['Ages'])
# 1)Create bins :Young(18-25),Adult(26-40),Senior(41+)
bins = [0,25,40,float('inf')]
labels = ['Young','Adult','Senior']
df['Age Group'] = pd.cut(df['Ages'], bins=bins, labels=labels)
print(df)
# 2)Assign category labels
df['Age Group'] = df['Age Group'].cat.add_categories(['Unknown'])
print(df)
# 3) Count number of records in each bin
age_group_counts = df['Age Group'].value_counts()
print(age_group_counts)

# 8. Correlation Analysis
data = {
    'Hours_studied':[2,4,6,8,10],
    'Marks':[40,50,65,80,95]
}
df = pd.DataFrame(data)
print(df)
# 1) Find correlation coeffient
correlation = df['Hours_studied'].corr(df['Marks'])
print("Correlation coefficient:",correlation)
# 2) Interpret the result
if correlation > 0:
    print("There is a positive correlation between hours studied and marks.")
elif correlation < 0:
    print("There is a negative correlation between hours studied and marks.")
else:
    print("There is no correlation between hours studied and marks.")
# 3) Plot a scatter plot
import matplotlib.pyplot as plt
plt.scatter(df['Hours_studied'],df['Marks'])
plt.xlabel('Hours Studied')
plt.ylabel('Marks')
plt.title('Hours Studied vs Marks')
plt.show()
# 4) Check if strong positive or negative correlation
if correlation > 0.7:
    print("There is a strong positive correlation.")
elif correlation < -0.7:
    print("There is a strong negative correlation.")
else:
    print("The correlation is weak.")

# 9) Large Dataset Type Question
data = {
    'Customer_ID':[1,2,3,4,5],
    'Age':[25,30,None,35,40],
    'Income':[50000,60000,55000,None,80000],
    'Gender':['Male','Female',None,'Female','Male'],
    'Purchase_Amount':[200,300,None,400,500],
    'City':['New York','Los Angeles','Chicago',None,'Houston']

}
df = pd.DataFrame(data)
print("Original Data :\n",df)
# 1) check for null values
print(df.isnull())
# 2) Replace missing income with median
df['Income'] = df['Income'].fillna(df['Income'].median())
print(df['Income'])
# 3) Remove duplicate customers
df_clean = df.drop_duplicates(subset='Customer_ID')
print(df_clean)
# 4) Detect outliers in purchase_amount
Q1 = df['Purchase_Amount'].quantile(0.25)
Q3 = df['Purchase_Amount'].quantile(0.75)
IQR = Q3 - Q1
l_limit = Q1 - 1.5 * IQR
u_limit = Q3 + 1.5 * IQR
outliers = df[(df['Purchase_Amount'] < l_limit) | (df['Purchase_Amount'] > u_limit)]
print("Outliers in Purchase Amount:")
print(outliers)
# 5) Standardize Income column
mean = df['Income'].mean()
std = df['Income'].std()
df['Income_Standardized'] = (df['Income'] - mean) / std
print(df['Income_Standardized'])
# 6) Encode Gender column
df['Gender_Encoded'] = df['Gender'].map({'Male':0,'Female':1})
print(df['Gender_Encoded'])
# 7) Find correlation between Income and purchase_amount
correlation = df['Income'].corr(df['Purchase_Amount'])
print("Correlation between Income and Purchase Amount:",correlation)
# 8) Create bins for Age
bins = [0,25,35,float('inf')]
labels = ['Young','Middle-aged','Senior']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
print(df['Age_Group'])
# 9)Save cleaned dataset as a CSV file
df.to_csv('cleaned_data.csv', index=False)
