
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load datasets
india = pd.read_csv("VISA_Details_2010-2013-oct.csv")
us = pd.read_csv("US Immigration Statistics (Ver 1.14.26).csv")
canada = pd.read_csv("Canadian Immigration Dataset.csv")

# 3. Understand data
print(india.head())
print(us.head())
print(canada.head())

print(india.info())
print(us.info())
print(canada.info())

# 4. Data Preprocessing

# INDIA
india.fillna(0, inplace=True)

# US DATASET CLEANING
us.columns = us.columns.str.strip()

for col in us.columns[1:]:
    us[col] = us[col].str.replace(',', '')
    us[col] = pd.to_numeric(us[col], errors='coerce')

us.fillna(0, inplace=True)

# CANADA DATASET CLEANING
# Drop unnecessary columns (ignore errors if not present)
canada.drop(['Unnamed: 0', 'Date', 'Date (hidden)', 
             'month_year', 'Date Full'], axis=1, errors='ignore', inplace=True)

# Convert numeric columns
for col in canada.columns:
    canada[col] = pd.to_numeric(canada[col], errors='coerce')

canada.fillna(0, inplace=True)

# Create Total column
canada['Total'] = canada.select_dtypes(include=['int64','float64']).sum(axis=1)

# Sort data
top_data = canada.sort_values(by='Total', ascending=False)

# -----------------------------
# 5. VISUALIZATIONS
# -----------------------------

# 1. Immigration trend (Canada - Year based)
year_data = canada.groupby('Year')['Invitations issued'].sum()

year_data.plot(kind='line', figsize=(10,5))
plt.title("Canada Immigration Trend")
plt.xlabel("Year")
plt.ylabel("Invitations")
plt.show()

# 2. Cumulative trend
year_data.cumsum().plot(kind='line')
plt.title("Cumulative Immigration Trend")
plt.show()

# 3. Distribution
plt.hist(canada['Invitations issued'], bins=20)
plt.title("Distribution of Invitations")
plt.show()

# 4. Compare programs
program_data = canada.groupby('Immigration program')['Invitations issued'].sum().sort_values(ascending=False)

program_data.head(10).plot(kind='bar')
plt.title("Top Immigration Programs")
plt.show()

# 5. Top 5 proportion
top5 = program_data.head(5)

top5.plot(kind='pie', autopct='%1.1f%%')
plt.title("Top 5 Programs Share")
plt.ylabel('')
plt.show()

# 6. Outliers
sns.boxplot(x=canada['Invitations issued'])
plt.title("Outliers Detection")
plt.show()

# 7. Scatter relationship
sns.scatterplot(x='Year', y='Invitations issued', data=canada)
plt.title("Year vs Invitations")
plt.show()

# 8. Bubble plot
plt.scatter(canada['Year'], canada['Invitations issued'],
            s=canada['Invitations issued']/10, alpha=0.5)

plt.xlabel("Year")
plt.ylabel("Invitations")
plt.title("Bubble Plot")
plt.show()

# 9. Top 5 bar
top5.plot(kind='bar', color='orange')
plt.title("Top 5 Programs")
plt.show()

# 10. Text visualization
for i in range(len(top5)):
    plt.text(i, top5.values[i], top5.index[i], fontsize=10 + i*2)

plt.bar(top5.index, top5.values)
plt.xticks(rotation=45)
plt.title("Programs by Size")
plt.show()

# 11. Pairplot
sns.pairplot(canada[['Year','Invitations issued','CRS score of lowest-ranked candidate invited']])
plt.show()

# 12. Heatmap
corr = canada[['Year','Invitations issued','CRS score of lowest-ranked candidate invited']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()