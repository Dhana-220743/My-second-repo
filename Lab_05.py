import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(os.getcwd())
print(os.listdir())
# 2)Loading dataset
df = pd.read_csv("Customer Purchasing Behaviors.csv",encoding="latin1")

# 3) Display the number of rows and columns 
print(df.shape)

# 4)Print the column names of the dataset
print(df.columns)

# 5)Display the first five rows
print(df.head())

# 6) Check the datatype of each column
print(df.dtypes)

# 7)Identify the number of missing values in each column
print(df.isnull().sum())

# 8)Fill missing values im numerical columns using the mean
df["user_id"] = df["user_id"].fillna(df["user_id"].mean())
df["age"] = df["age"].fillna(df["age"].mean())
df["annual_income"] = df["annual_income"].fillna(df["annual_income"].mean())
df["purchase_amount"] = df["purchase_amount"].fillna(df["purchase_amount"].mean())
df["purchase_frequency"] = df["purchase_frequency"].fillna(df["purchase_frequency"].mean())

# 9)Fill missing values in categorical columns using the mode
df["region"]=df["region"].fillna(df["region"].mode()[0])

#10) verify that there are no missing values remaining
print(df.isnull().sum())

# 11) Calculate the mean for all numeric columns
print(df[["user_id","age","annual_income","purchase_amount","purchase_frequency"]].mean())

# 12) Calculate the median for all numeric columns
print(df[["user_id","age","annual_income","purchase_amount","purchase_frequency"]].median())

# 13)Calculate the standard deviation for all numerical columns.
print(df[["user_id","age","annual_income","purchase_amount","purchase_frequency"]].std())
#14)Find the maximum values for numerical columns.
print(df[["user_id","age","annual_income","purchase_amount","purchase_frequency"]].max())
#14)Find the minimum values for numerical columns.
print(df[["user_id","age","annual_income","purchase_amount","purchase_frequency"]].min())
#15)Generate a summary using describe().
print(df.describe())
#16)Create a histogram for the purchase amount column.
plt.hist(df['purchase_amount'],bins=10)
plt.xlabel('Purchase_amount')
plt.ylabel('purchase_frequency')
plt.title('Histogram of Purchase Amount')
plt.show()

#17)Create a bar chart showing the count of customers by product category.
region_counts = df["region"].value_counts()
region_counts.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Customer Count")
plt.title("Customers by Region")
plt.show()
#18)Create a box plot for the purchase amount column.
plt.boxplot(df['purchase_amount'])
plt.ylabel('purchase_amount')
plt.title('Box plot of purchase amount')
plt.show()
#19)Create a scatter plot between age and purchase amount.
plt.scatter(df['age'],df['purchase_amount'])
plt.xlabel('age')
plt.ylabel('purchase_amount')
plt.title('Age vs Purchase amount')
plt.show()
#20)Display a correlation heatmap for numerical columns.
corr = df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
