#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary libraries for data analysis and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast
from datetime import datetime
from sklearn.preprocessing import LabelEncoder


# In[2]:


# Reading the CSV file containing opportunity wise data and storing it in a DataFrame
opps_su_comp_data = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Excelerate DA Internship\Opportunity Wise Data.csv')

# Printing the first few rows of the DataFrame 'opps_su_comp_data'
print(opps_su_comp_data)


# In[3]:


# Display information about the DataFrame structure and data types
opps_su_comp_data.info()


# In[4]:


# Calculating the number of null (missing) values in each column of the DataFrame 'opps_su_comp_data'
opps_su_comp_data_null = opps_su_comp_data.isna().sum()

# Printing the number of null values for each column
print(opps_su_comp_data_null)


# In[5]:


# Display summary statistics of numerical columns in the DataFrame
print(opps_su_comp_data.describe())


# In[6]:


# Convert DataFrame columns to a list
opps_su_comp_data_cols = opps_su_comp_data.columns.tolist()

# Display the list of columns
print(opps_su_comp_data_cols)


# In[7]:


# Convert the 'Opportunity End Date' column to datetime format
opps_su_comp_data['Opportunity End Date'] = pd.to_datetime(opps_su_comp_data['Opportunity End Date'])

# Assign the values from 'Graduation Date(YYYY MM)' to 'Graduation Date'
opps_su_comp_data['Graduation Date'] = pd.to_datetime(opps_su_comp_data['Graduation Date(YYYY MM)'], format='%Y %m', errors='coerce')

# Drop the 'Graduation Date(YYYY MM)' column
opps_su_comp_data.drop('Graduation Date(YYYY MM)', axis=1, inplace=True)

# Replace '24' with '00' in the 'Apply Date' column as text
opps_su_comp_data['Apply Date'] = opps_su_comp_data['Apply Date'].str.replace(', 24:', ', 00:')
opps_su_comp_data['Apply Date'] = pd.to_datetime(opps_su_comp_data['Apply Date'])
opps_su_comp_data['Opportunity Start Date'] = pd.to_datetime(opps_su_comp_data['Opportunity Start Date'])

# Replace 'Accr, Ghana' with 'Accra' in the 'State' column
# Replace 'A' with 'Accra' in the 'City' column
replace_dict = {'State': {'Accr, Ghana': 'Accra'}, 'City': {'A': 'Accra'}}
opps_su_comp_data.replace(replace_dict, inplace=True)

# Replace "Don't Want To Specify" with "Don't Want To Specify" in the 'Gender' column
opps_su_comp_data['Gender'] = opps_su_comp_data['Gender'].replace("Don'T Want To Specify", "Don't Want To Specify")

# Replace "Don't Want To Specify" with "Don't Want To Specify" in the 'Gender' column
opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].replace('Oth', 'Others')

# Replace "Don't Want To Specify" with "Don't Want To Specify" in the 'Gender' column
opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].replace('Otheraassss', 'Others')

# Replace "Don't Want To Specify" with "Don't Want To Specify" in the 'Gender' column
opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].replace('Aa', 'Applied Arts')

# Replace "Don't Want To Specify" with "Don't Want To Specify" in the 'Gender' column
opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].replace('jknhk', 'Unknown')

opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].str.replace('Bsc in ', '')

opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].str.replace('PHD in ', '')

opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].str.replace('Phd', 'Unknown')

# Replace various forms of 'Bsc' with '' in the 'Current/Intended Major' column
opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].str.replace(r'(?i)Bsc\s*(in)?\s*(CS|Computer Science)?', '', regex=True)

# Replace various forms of 'B TECH' with '' in the 'Current/Intended Major' column
opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].str.replace(r'(?i)B\s*TECH\s*(in)?', '', regex=True)

# Replace "Don't Want To Specify" with "Don't Want To Specify" in the 'Gender' column
opps_su_comp_data['Current/Intended Major'] = opps_su_comp_data['Current/Intended Major'].replace('jknhk', 'Unknown')


# In[8]:


# Fill missing values in the 'Gender' column with the mode value
opps_su_comp_data['Gender'].fillna(opps_su_comp_data['Gender'].mode()[0], inplace=True)

# Fill missing values in the 'City' column with the mode value
opps_su_comp_data['City'].fillna(opps_su_comp_data['City'].mode()[0], inplace=True)

# Fill missing values in the 'State' column with the mode value
opps_su_comp_data['State'].fillna(opps_su_comp_data['State'].mode()[0], inplace=True)

# Fill missing values in the 'Zip Code' column with 'Unknown'
opps_su_comp_data['Zip Code'].fillna(opps_su_comp_data['Zip Code'].mode()[0], inplace=True)

# Fill missing values in the 'Graduation Date' column with the mode value
opps_su_comp_data['Graduation Date'].fillna(opps_su_comp_data['Graduation Date'].mode()[0], inplace=True)

# Fill missing values in the 'Current Student Status' column with the mode value
opps_su_comp_data['Current Student Status'].fillna(opps_su_comp_data['Current Student Status'].mode()[0], inplace=True)

# Fill missing values in the 'Current/Intended Major' column with 'Unknown'
opps_su_comp_data['Current/Intended Major'].fillna(opps_su_comp_data['Current/Intended Major'].mode()[0], inplace=True)

# Fill missing values in the 'Opportunity Start Date' column with the mode value
opps_su_comp_data['Opportunity Start Date'].fillna(opps_su_comp_data['Opportunity Start Date'].mode()[0], inplace=True)

# Fill missing values in the 'Reward Amount' column with 0
opps_su_comp_data['Reward Amount'].fillna(0, inplace=True)

# Fill missing values in the 'Badge Id' column with 'None'
opps_su_comp_data['Badge Id'].fillna('None', inplace=True)

# Fill missing values in the 'Badge Name' column with 'None'
opps_su_comp_data['Badge Name'].fillna('None', inplace=True)

# Fill missing values in the 'Skill Points Earned' column with 0
opps_su_comp_data['Skill Points Earned'].fillna(0, inplace=True)

# Fill missing values in the 'Skills Earned' column with 'None'
opps_su_comp_data['Skills Earned'].fillna('None', inplace=True)


# In[9]:


# Calculating the number of null (missing) values in each column of the DataFrame 'opps_su_comp_data'
opps_su_comp_data_null = opps_su_comp_data.isna().sum()

# Printing the number of null values for each column
print(opps_su_comp_data_null)


# In[10]:


# Replace entries in the 'Zip Code' column where the number of characters is less than 5 or more than 10 with 'Unknown'
opps_su_comp_data.loc[(opps_su_comp_data['Zip Code'].str.len() < 5) | (opps_su_comp_data['Zip Code'].str.len() > 10), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where all characters are alphabets with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.isalpha(), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains spaces with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(' '), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains more than 3 consecutive alphabets with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(r'[A-Za-z]{4,}'), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it starts with special characters with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(r'^[^A-Za-z0-9]'), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains more than 10 characters and does not include '-'
opps_su_comp_data.loc[(opps_su_comp_data['Zip Code'].str.len() > 10) & (~opps_su_comp_data['Zip Code'].str.contains('-')), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where the number of characters before '-' is less than 5 with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.split('-').str[0].str.len() < 5, 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains a decimal point or exponential with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(r'[.eE]'), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains more than two '-' with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.count('-') > 2, 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where '-' is the last character with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.endswith('-'), 'Zip Code'] = 'Unknown'

# Capitalize the entire entry in the 'Zip Code' column if the first character is in lowercase
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].apply(lambda x: x.capitalize() if x and x[0].islower() else x)

# Display unique values in the 'Zip Code' column after the replacement
print(opps_su_comp_data['Zip Code'].unique())


# In[11]:


# Replace entries in the 'Zip Code' column where the number of characters is less than 5 with 'Unknown'
opps_su_comp_data.loc[(opps_su_comp_data['Zip Code'].str.len() < 5) | (opps_su_comp_data['Zip Code'].str.len() > 10), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where all characters are alphabets with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.isalpha(), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains spaces with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(' '), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains more than 3 consecutive alphabets with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(r'[A-Za-z]{4,}'), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it starts with special characters with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(r'^[^A-Za-z0-9]'), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains more than 10 characters and does not include '-'
opps_su_comp_data.loc[(opps_su_comp_data['Zip Code'].str.len() > 10) & (~opps_su_comp_data['Zip Code'].str.contains('-')), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where the number of characters before '-' is less than 5
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.split('-').str[0].str.len() < 5, 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains a decimal point or exponential
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.contains(r'[.eE]'), 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where it contains more than two '-'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.count('-') > 2, 'Zip Code'] = 'Unknown'

# Replace entries in the 'Zip Code' column where '-' is the last character with 'Unknown'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].str.endswith('-'), 'Zip Code'] = 'Unknown'

# Capitalize the entire entry in the 'Zip Code' column if the first character is in lowercase
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].apply(lambda x: x.capitalize() if x and x[0].islower() else x)

# Replace 'city' with 'Saint Louis' where 'Zip Code' is equal to '63108', '63103', or '63101'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].isin(['63108', '63103', '63101', '63146', '61303']), 'City'] = 'Saint Louis'

# Replace '63018' with '63108' in the 'Zip Code' column
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('63018', '63108')
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('61303', '63103')
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('613108', '63108')
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('400101', '40010')
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('500068', '50006')
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('50351', '53051')
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('583101', '58310')
opps_su_comp_data['Zip Code'] = opps_su_comp_data['Zip Code'].replace('500039', '50003')

# Replace zip code where it's 'Unknown' and city is 'Saint Louis'
opps_su_comp_data.loc[(opps_su_comp_data['Zip Code'] == 'Unknown') & (opps_su_comp_data['City'] == 'Saint Louis'), 'Zip Code'] = '63108'

# Replace 'Alden' in the 'City' column where 'Zip Code' is '50006'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'] == '50006', 'City'] = 'Alden'

# Replace 'Agate' in the 'City' column where 'Zip Code' is '58310'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'] == '58310', 'City'] = 'Agate'

# Replace 'Adel' in the 'City' column where 'Zip Code' is '50003'
opps_su_comp_data.loc[opps_su_comp_data['Zip Code'] == '50003', 'City'] = 'Adel'

# Replace zip codes based on specified conditions
opps_su_comp_data.loc[opps_su_comp_data['City'] == 'Morganville', 'Zip Code'] = '07751'
opps_su_comp_data.loc[opps_su_comp_data['City'] == 'Avon', 'Zip Code'] = '46123'
opps_su_comp_data.loc[opps_su_comp_data['City'] == 'Boston', 'Zip Code'] = '02108'
opps_su_comp_data.loc[opps_su_comp_data['City'] == 'Brookline', 'Zip Code'] = '02445'

# Replace values in the 'City' column
opps_su_comp_data['City'].replace({'New': 'New Jersey', 'Hchudhbc': 'Haysville'}, inplace=True)

# Define the mapping of cities to their corresponding zip codes
city_zip_mapping = {
    'Hillsborough': '08844',
    'Oakdale': '95361',
    'Byfield': '01922',
    'Hartford': '06074',
    'Manalapan': '07726',
    'Boston': '02108',
    'Canton': '48187',
    'Haysville': '67060',
    'Brookline': '02445',
    'Cambridge': '02138',
    'New Brunswick': '08901',
    'Ocean Township': '07755',
    'Pay': '51510',
    'Helmetta': '08828',
    'Greenwich': '06830',
    'Newton': '02495',
    'New Fairfield': '06812',
    'Glen Rock': '07452',
    'Waterbury': '06708',
    'Holmdel': '07733',
    'Sacramento': '94203',
    'East Haven': '06512',
    'Ellington': '06029',
    'West Orange': '07052',
    'Morganville': '07751',
    'Franklin': '37027',
    'Edison': '08817',
    'Rahway': '07065',
    'Walpole': '02081',
    'Iselin': '08830',
    'Denville': '07834',
    'New Jersey': '07001',
    'Merrimack': '03054',
    'Jersey City': '07302',
    'Plainsboro': '08536',
    'Marlboro': '07746',
    'Springfield': '65619',
    'Oradell': '07649',
    'Cranston': '02920',
    'West Haven': '06516',
    'Coppell': '76051'
}

# Replace zip codes based on the city mapping
opps_su_comp_data['Zip Code'] = opps_su_comp_data.apply(lambda row: city_zip_mapping.get(row['City'], row['Zip Code']), axis=1)

# Replace zip code and country based on the city condition
opps_su_comp_data.loc[opps_su_comp_data['City'] == 'Hasilpur', 'Zip Code'] = '63000'
opps_su_comp_data.loc[opps_su_comp_data['City'] == 'Hasilpur', 'Country'] = 'India'

opps_su_comp_data.loc[opps_su_comp_data['Zip Code'].isin(['63108', '40010', '50006', '53051', '58310', '50003']), 'Country'] = 'United States'

# Drop rows where zip is '75002'
opps_su_comp_data = opps_su_comp_data[opps_su_comp_data['Zip Code'] != '75002']

# Display unique values in the 'Zip Code' column after the replacement
print(opps_su_comp_data['Zip Code'].unique())


# In[12]:


# Apply a function to each column in the DataFrame
# Use a lambda function to check if the column's dtype is 'object' (strings)
opps_su_comp_data = opps_su_comp_data.apply(
    lambda x: x.str.strip() if x.dtype == 'object' else x
)


# In[13]:


# Checking for and counting duplicated rows in the DataFrame 'opps_su_comp_data'
opps_su_comp_data_dupl = opps_su_comp_data.duplicated().sum()

# Print the count of duplicated rows
print('Duplicates: ', opps_su_comp_data_dupl)


# In[14]:


# List of selected string columns
selected_columns = ['Opportunity Name', 'Opportunity Category', 'Gender', 'City', 'State', 'Country', 'Current Student Status', 'Status Description', 'Skills Earned']

# Apply title case only to string columns in the DataFrame
opps_su_comp_data[selected_columns] = opps_su_comp_data[selected_columns].apply(lambda x: x.str.title() if x.dtype == 'O' else x)


# In[15]:


# Filter numerical columns
#numerical_cols = user_data.select_dtypes(include='number')

# Calculate the correlation matrix for numerical columns
correlation_matrix =  opps_su_comp_data.select_dtypes(include='number').corr()

print(correlation_matrix)

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Create a heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Show the plot
plt.title("Correlation Matrix Heatmap")
plt.show()


# In[16]:


# Numerical column of interest
numerical_column = ['Reward Amount', 'Skill Points Earned']

# Visualize the distribution with a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=[opps_su_comp_data['Reward Amount'], opps_su_comp_data['Skill Points Earned']], showfliers=True, flierprops=dict(marker='o', markersize=8, markerfacecolor='red', markeredgecolor='red'))
plt.title('Box Plot for Reward Amount and Skill Points Earned')
plt.show()


# In[17]:


# Create a mapping dictionary for the 'Gender' column
gender_mapping = {'Male': 0, 'Female': 1, 'Other': 2, "Don'T Want To Specify": 3}

# Map the 'Gender' column using the provided mapping
opps_su_comp_data['Gender_encoded'] = opps_su_comp_data['Gender'].map(gender_mapping)

# Display the resulting DataFrame with the mapped 'Gender' column
print(opps_su_comp_data[['Gender', 'Gender_encoded']])


# In[18]:


# Create a mapping dictionary for the 'Gender' column
Opportunity_Category_mapping = {'Event': 0, 'Course': 1, 'Competition': 2, 'Internship': 3, 'Engagement': 4}

# Map the 'Gender' column using the provided mapping
opps_su_comp_data['Opportunity Category_encoded'] = opps_su_comp_data['Opportunity Category'].map(Opportunity_Category_mapping)

# Display the resulting DataFrame with the mapped 'Gender' column
print(opps_su_comp_data[['Opportunity Category', 'Opportunity Category_encoded']])


# In[19]:


# Create a mapping dictionary for the 'Current Student Status' column
current_student_status_mapping = {'High School Student': 0, 'Undergraduate Student': 1, 'Graduate Program Student': 2, 'Not In Education': 3}

# Map the 'Current Student Status' column using the provided mapping
opps_su_comp_data['Current Student Status_encoded'] = opps_su_comp_data['Current Student Status'].map(current_student_status_mapping)

# Display the resulting DataFrame with the mapped 'Current Student Status' column
print(opps_su_comp_data[['Current Student Status', 'Current Student Status_encoded']])


# In[20]:


# Create a mapping dictionary for the 'Current Student Status' column
Status_Description_mapping = {'Not Started': 0, 'Rewards Award': 1, 'Team Allocated': 2, 'Started': 3, 'Withdraw': 4, 'Dropped Out': 5, 'Rejected': 6, 'Applied': 7}

# Map the 'Current Student Status' column using the provided mapping
opps_su_comp_data['Status Description_encoded'] = opps_su_comp_data['Status Description'].map(Status_Description_mapping)

# Display the resulting DataFrame with the mapped 'Current Student Status' column
print(opps_su_comp_data[['Status Description', 'Status Description_encoded']])


# In[21]:


# Convert the string representation of a list to an actual list
opps_su_comp_data['Skills Earned'] = opps_su_comp_data['Skills Earned'].apply(ast.literal_eval)

# Explode the 'Skills Earned' column into separate rows
opps_su_comp_data_exp = opps_su_comp_data.explode('Skills Earned')

# Reset the index to ensure correct row indexing
opps_su_comp_data_exp.reset_index(drop=True, inplace=True)

# Fill missing values in the 'Skills Earned' column with 'None'
opps_su_comp_data_exp['Skills Earned'].fillna('None', inplace=True)


# In[22]:


# Exporting the DataFrame to a CSV file
opps_su_comp_data_exp.to_csv(r'C:\Users\HP\OneDrive\Desktop\Excelerate DA Internship\opps_su_comp_data_exp.csv', index=False)


# In[ ]:




