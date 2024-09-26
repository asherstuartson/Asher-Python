#!/usr/bin/env python
# coding: utf-8

# In[155]:


# Importing necessary libraries for data analysis and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import uuid
import ast


# In[156]:


# Reading the CSV file containing user data and storing it in a DataFrame 'user_data'
user_data = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Excelerate DA Internship\UserData.csv')

user_data.head()


# In[157]:


# Add a new column 'Signup_ID' and generate unique IDs
user_data['Signup_ID'] = 'SU_' + user_data.apply(lambda _: uuid.uuid4().hex[:12], axis=1)

# Reorder columns with 'Signup_ID' as the first column
user_data = user_data[['Signup_ID', 'PreferredSponsors', 'Gender', 'Country', 'Degree', 'Sign Up Date', 'city', 'zip', 'isFromSocialMedia']]


# In[158]:


# Convert DataFrame columns to a list
user_data_cols = user_data.columns.tolist()

# Display the list of columns
print(user_data_cols)


# In[159]:


# Convert the 'Sign Up Date' column to datetime format
user_data['Sign Up Date'] = pd.to_datetime(user_data['Sign Up Date'],format='%Y-%m-%dT%H:%M:%S.%fZ', utc=True)

# Display information about the DataFrame 'user_data'
user_data.info()


# In[160]:


# Calculating the number of null (missing) values in each column of the DataFrame 'user_data'
user_data_null = user_data.isna().sum()

# Printing the number of null values for each column
print(user_data_null)


# In[161]:


# Fill missing values in the 'Gender' column with 'Unknown'
user_data['Gender'].fillna(user_data['Gender'].mode()[0], inplace=True)

# Fill missing values in the 'Country' column with the mode (most frequent value)
user_data['Country'].fillna(user_data['Country'].mode()[0], inplace=True)

# Fill missing values in the 'Degree' column with 'Unknown'
user_data['Degree'].fillna(user_data['Degree'].mode()[0], inplace=True)

# Fill missing values in the 'city' column with 'Unknown'
user_data['city'].fillna(user_data['city'].mode()[0], inplace=True)

# Fill missing values in the 'zip' column with 'Unknown'
user_data['zip'].fillna(user_data['zip'].mode()[0], inplace=True)

# Fill missing values in the 'isFromSocialMedia' column with the string 'True'
user_data['isFromSocialMedia'].fillna(user_data['isFromSocialMedia'].mode()[0], inplace=True)


# In[162]:


# Replace entries in the 'zip' column where the number of characters is less than 5 with 'Unknown'
user_data.loc[(user_data['zip'].str.len() < 5) | (user_data['zip'].str.len() > 10), 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where all characters are alphabets with 'Unknown'
user_data.loc[user_data['zip'].str.isalpha(), 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where it contains spaces with 'Unknown'
user_data.loc[user_data['zip'].str.contains(' '), 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where it contains more than 3 consecutive alphabets with 'Unknown'
user_data.loc[user_data['zip'].str.contains(r'[A-Za-z]{4,}'), 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where it starts with special characters with 'Unknown'
user_data.loc[user_data['zip'].str.contains(r'^[^A-Za-z0-9]'), 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where it contains more than 10 characters and does not include '-'
user_data.loc[(user_data['zip'].str.len() > 10) & (~user_data['zip'].str.contains('-')), 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where the number of characters before '-' is less than 5
user_data.loc[user_data['zip'].str.split('-').str[0].str.len() < 5, 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where it contains a decimal point or exponential
user_data.loc[user_data['zip'].str.contains(r'[.eE]'), 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where it contains more than two '-'
user_data.loc[user_data['zip'].str.count('-') > 2, 'zip'] = 'Unknown'

# Replace entries in the 'zip' column where '-' is the last character with 'Unknown'
user_data.loc[user_data['zip'].str.endswith('-'), 'zip'] = 'Unknown'

# Capitalize the entire entry in the 'zip' column if the first character is in lowercase
user_data['zip'] = user_data['zip'].apply(lambda x: x.capitalize() if x and x[0].islower() else x)

# Replace 'city' with 'Saint Louis' where 'zip' is equal to '63108', '63103', or '63101'
user_data.loc[user_data['zip'].isin(['63108', '63103', '63101', '63146', '61303']), 'city'] = 'Saint Louis'

# Replace '63018' with '63108' in the 'zip' column
user_data['zip'] = user_data['zip'].replace('63018', '63108')
user_data['zip'] = user_data['zip'].replace('61303', '63103')
user_data['zip'] = user_data['zip'].replace('613108', '63108')
user_data['zip'] = user_data['zip'].replace('400101', '40010')
user_data['zip'] = user_data['zip'].replace('500068', '50006')
user_data['zip'] = user_data['zip'].replace('50351', '53051')
user_data['zip'] = user_data['zip'].replace('583101', '58310')
user_data['zip'] = user_data['zip'].replace('500039', '50003')

# Replace zip code where it's 'Unknown' and city is 'Saint Louis'
user_data.loc[(user_data['zip'] == 'Unknown') & (user_data['city'] == 'Saint Louis'), 'zip'] = '63108'

# Replace 'Alden' in the 'city' column where 'zip' is '50006'
user_data.loc[user_data['zip'] == '50006', 'city'] = 'Alden'

# Replace 'Alden' in the 'city' column where 'zip' is '50006'
user_data.loc[user_data['zip'] == '58310', 'city'] = 'Agate'

# Replace 'Alden' in the 'city' column where 'zip' is '50006'
user_data.loc[user_data['zip'] == '58310', 'city'] = 'Agate'
user_data.loc[user_data['zip'] == '50003', 'city'] = 'Adel'

# Replace zip codes based on specified conditions
user_data.loc[user_data['city'] == 'Morganville', 'zip'] = '07751'
user_data.loc[user_data['city'] == 'Avon', 'zip'] = '46123'
user_data.loc[user_data['city'] == 'Boston', 'zip'] = '02108'
user_data.loc[user_data['city'] == 'Brookline', 'zip'] = '02445'

# Replace values in the 'city' column
user_data['city'].replace({'New': 'New Jersey', 'Hchudhbc': 'Haysville'}, inplace=True)


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
user_data['zip'] = user_data.apply(lambda row: city_zip_mapping.get(row['city'], row['zip']), axis=1)

# Replace zip code and country based on the city condition
user_data.loc[user_data['city'] == 'Hasilpur', 'zip'] = '63000'
user_data.loc[user_data['city'] == 'Hasilpur', 'Country'] = 'India'

user_data.loc[user_data['zip'].isin(['63108', '40010', '50006', '53051', '58310', '50003']), 'Country'] = 'United States'

# Drop rows where zip is '75002'
user_data = user_data[user_data['zip'] != '75002']

# Display unique values in the 'zip' column after the replacement
print(user_data['zip'].unique())


# In[163]:


# Apply a function to each column in the DataFrame
# Use a lambda function to check if the column's dtype is 'object' (strings)
user_data = user_data.apply(
    lambda x: x.str.strip() if x.dtype == 'object' else x
)


# In[164]:


# Checking for and counting duplicated rows in the DataFrame 'prod_sal_dat'
user_data_dupl = user_data.duplicated().sum()

# Print the count of duplicated rows
print('Duplicates: ', user_data_dupl)


# In[165]:


# List of columns to apply sentence case
selected_columns = ['PreferredSponsors', 'Gender', 'Country', 'Degree', 'city']

# Apply title case to selected string columns in the DataFrame
user_data[selected_columns] = user_data[selected_columns].apply(lambda x: x.str.title())

# Replace entries in the 'zip' column where the value starts with '-' with the value after '-'
user_data.loc[user_data['zip'].str.startswith('-'), 'zip'] = user_data['zip'].str.split('-', n=1).str[1]


# # Data Preprocessing

#     # Feature Engineering

# In[166]:


user_data['Age'] = (pd.Timestamp.now(tz='UTC') - user_data['Sign Up Date']).dt.days
user_data['Signup Year'] = user_data['Sign Up Date'].dt.year
user_data['Signup Month'] = user_data['Sign Up Date'].dt.month
user_data['Signup Day'] = user_data['Sign Up Date'].dt.day


# In[167]:


# Display information about the DataFrame 'user_data'
user_data.info()


# In[168]:


# Numerical column of interest
numerical_column = 'Age'

# Visualize the distribution with a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x=user_data[numerical_column], showfliers=True, flierprops=dict(marker='o', markersize=8, markerfacecolor='red', markeredgecolor='red'))
plt.title('Box Plot for Age')
plt.show()


# In[169]:


# Calculate the median and mean values of the 'revenue' column
Days_SSU_median = user_data[numerical_column].median()
Days_SSU_mean = user_data[numerical_column].mean()

# Visualize the distribution with a histogram
plt.figure(figsize=(10, 6))
sns.histplot(user_data[numerical_column], bins=30, kde=True)

# Add vertical lines for mean and median on the histogram
plt.axvline(Days_SSU_mean, color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(Days_SSU_median, color='green', linestyle='dashed', linewidth=2, label='Median')

# Add text annotations for mean and median values
plt.text(Days_SSU_mean, plt.ylim()[1]*0.9, f'Mean: {Days_SSU_mean:.2f}', color='red')
plt.text(Days_SSU_median, plt.ylim()[1]*0.85, f'Median: {Days_SSU_median:.2f}', color='green')

plt.title('Histogram for Age')
plt.xlabel('Age')
plt.show()


# In[170]:


# Identify and remove extreme outliers in the 'Age' column
Q1 = user_data['Age'].quantile(0.25)
Q3 = user_data['Age'].quantile(0.75)
IQR = Q3 - Q1
age_outlier_threshold = 1.5 * IQR

user_data = user_data[(user_data['Age'] >= Q1 - age_outlier_threshold) & (user_data['Age'] <= Q3 + age_outlier_threshold)]

print(user_data)


# In[171]:


# Create a mapping dictionary for the 'Degree' column
degree_mapping = {'Undergraduate Student': 1, 'Graduate Program Student': 2, 'High School Student': 3, 'Not In Education': 4, 'Not Provided': 5}

# Map the 'Degree' column using the provided mapping
user_data['Degree_encoded'] = user_data['Degree'].map(degree_mapping)

# Display the resulting DataFrame with the mapped 'Degree' column
print(user_data[['Degree','Degree_encoded']])


# In[172]:


# Create a mapping dictionary for the 'Gender' column
gender_mapping = {'Male': 0, 'Female': 1, 'Other': 2, "Don'T Want To Specify": 3}

# Map the 'Gender' column using the provided mapping
user_data['Gender_encoded'] = user_data['Gender'].map(gender_mapping)

# Display the resulting DataFrame with the mapped 'Gender' column
print(user_data[['Gender', 'Gender_encoded']])


# In[173]:


# Create a LabelEncoder object
label_encoder = LabelEncoder()

# Fit and transform the 'isFromSocialMedia' column
user_data['isFromSocialMedia_encoded'] = label_encoder.fit_transform(user_data['isFromSocialMedia'])

# Display the resulting DataFrame with the encoded 'isFromSocialMedia' column
print(user_data[['isFromSocialMedia', 'isFromSocialMedia_encoded']])


# In[174]:


# Convert the string representation of a list to an actual list
user_data['PreferredSponsors'] = user_data['PreferredSponsors'].apply(ast.literal_eval)

# Explode the 'PreferredSponsors' column into separate rows
user_data_exp = user_data.explode('PreferredSponsors')

# Reset the index to ensure correct row indexing
user_data_exp.reset_index(drop=True, inplace=True)

# Exporting the DataFrame to a CSV file
user_data_exp.to_csv(r'C:\Users\HP\OneDrive\Desktop\Excelerate DA Internship\user_data_exp.csv', index=False)


# In[ ]:





# In[ ]:




