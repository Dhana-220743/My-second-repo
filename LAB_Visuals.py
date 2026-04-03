import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

canada_df = pd.read_csv("Canadian Immigration Dataset.csv")
usa_df = pd.read_csv("US Immigration Statistics (Ver 1.14.26).csv")
visa_df = pd.read_csv("VISA_Details_2010-2013-oct.csv")
'''
print(canada_df.head())
print(usa_df.head())
print(visa_df.head())
Basic info 
print(canada_df.info())
print(usa_df.info())
print(visa_df.info())

 Finding missing values'''
print("Missing values in Canada:",canada_df.isnull().sum())
print("Missing values in USA:",usa_df.isnull().sum())
print("Missing values in India Visa:",visa_df.isnull().sum())
 
print(usa_df.dropna(inplace=True))


'''1)  To visualize immigration trends over the years for a selected country.'''
canada_df.rename(columns={'Country':'Country'},inplace=True)
canada_melted = canada_df.melt(
    id_vars=['Country'],
    var_name = 'Year',
    value_name='Value'

)
canada_melted = canada_melted[canada_melted['Year'].str.isnumeric()]

print(usa_df.columns)
usa_df.rename(columns={
    'country_name': 'Country',
    'year': 'Year',
    'value': 'Value'
}, inplace=True)
print(visa_df.columns)
visa_df.rename(columns={
    'Nationality': 'Country',
    'Year': 'Year'
}, inplace=True)

# If no direct "Value", count records
visa_grouped = visa_df.groupby(['Country', 'Year']).size().reset_index(name='Value')
final_df = pd.concat([canada_melted, usa_df, visa_grouped], ignore_index=True)
