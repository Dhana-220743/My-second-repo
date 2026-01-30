import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

r = pd.read_csv("IMDB-Movie-Data.csv")
print(r)
# Load and Explore dataset
# returns first five rows
print(r.head())
#returns last five rows
print(r.tail())
#returns number of rows and columns
print(r.shape) 
#returns columns names
print(r.columns)

print(r.dtypes)
print(r.info())
#identify the missing values
print(r.isnull().sum())

#Data cleaning
#removing duplicates
print(r.dropna()) 
#filling missing values
r['Revenue (Millions)'] = r ['Revenue (Millions)'].fillna(0)
print( r['Revenue (Millions)']) 

print(r.drop_duplicates()) 

#Create Target label
r['label'] = r['Rating'].apply(lambda x: 'High' if x>=7 else 'Low')
print(r[['Title','Rating','label']].head())

#Feature Engineering
feature = r[['Runtime (Minutes)','Votes','Revenue (Millions)','Metascore']]
tgt = r['label']
print(tgt)

feature = feature.fillna(0)
print(feature)

#encode categorical data
le = LabelEncoder()
feature['Genre'] = le.fit_transform(r['Genre'])
print(feature['Genre'])
print(feature.head())

#Exploratory Data Analysis
plt.scatter(r['Votes'], r['Rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Rating vs Votes')
plt.show()

plt.scatter(r['Revenue (Millions)'], r['Rating'])
plt.xlabel('Revenue (Millions)')
plt.ylabel('Rating')
plt.title('Rating vs Revenue')
plt.show()

plt.scatter(r['Runtime (Minutes)'],r['Rating'])
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Rating')
plt.title('Rating vs Runtime')
plt.show()

r['Genre'].value_counts().plot(kind="bar")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Genre Distribution")
plt.show()
