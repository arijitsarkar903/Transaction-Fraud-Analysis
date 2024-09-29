

# importing all the required modules
import pyodbc
import pandas as pds
import numpy as num
import matplotlib.pyplot as plt
import seaborn as sea
# ignoring warnings
import warnings
warnings.filterwarnings("ignore")

# Importing financial_data table

# Defining the connection to the SQL Server
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DESKTOP-0FIICAT\SQLEXPRESS01;'
    r'DATABASE=capstone;'
    r'Trusted_Connection=yes;'
)

# Making connection to the SQL Server
conn = pyodbc.connect(conn_str)

# Query for importing the financial_data
query1 = "SELECT * FROM financial_data"

# Reading the query result into a Pandas DataFrame
financial_df = pds.read_sql(query1, conn)

# Print the first few rows of the DataFrame to confirm
print(financial_df.head())

# Close the connection
conn.close()

# Establish a connection to the SQL Server
conn = pyodbc.connect(conn_str)

# Query to import Customer_Details
query2 = "SELECT * FROM Customer_Details"

# Read the query result into a Pandas DataFrame
Customer_df = pds.read_sql(query2, conn)

# Print the first few rows of the DataFrame to confirm
print(Customer_df.head())

# Close the connection
conn.close()

# Establish a connection to the SQL Server
conn = pyodbc.connect(conn_str)

# Query to import merchant_details
query3 = "SELECT * FROM Merchant_Details"

# Read the query result into a Pandas DataFrame
merchant_df = pds.read_sql(query3, conn)

# Print the first few rows of the DataFrame to confirm
print(merchant_df.head())

# Close the connection
conn.close()

# Establish a connection to the SQL Server
conn = pyodbc.connect(conn_str)

# Query to import another table
query4 = "SELECT * FROM location_details"

# Read the query result into a Pandas DataFrame
location_df = pds.read_sql(query4, conn)

# Print the first few rows of the DataFrame to confirm
print(location_df.head())

# Close the connection
conn.close()

# Establish a connection to the SQL Server
conn = pyodbc.connect(conn_str)

# Query to import another table
query4 = "SELECT * FROM Card_Details"

# Read the query result into a Pandas DataFrame
Card_df = pds.read_sql(query4, conn)

# Print the first few rows of the DataFrame to confirm
print(Card_df.head())

# Close the connection
conn.close()

"""Showing all data"""

# Removing the unnecessary columns
fin_df = financial_df.drop(columns=['transaction_time', 'transaction_description'])

fin_df.head(10)

merchant_df.head(10)

#showing top 5 rows of the data
Customer_df.head()

Card_df.head()

location_df.head()

"""Null Values Checking"""

# Checking for the null values
fin_df.isnull().sum()

"""Merging Data"""

# Merging the Financial Data with the Customer Data
merged_1 = fin_df.merge(Customer_df, on='customer_id', how='left')

merged_1.head()

# Merging the above data with Merchant Details data
merged_2 = merged_1.merge(merchant_df, on='merchant_id', how='left')

merged_2.head()

# Merging the above data with Merchant Details data
merged_3 = merged_2.merge(location_df, on='location_ID', how='left')

merged_3.head()

# Merging previous merged data with the Card Details data
final_data = merged_3.merge(Card_df, on='card_ID', how='left')

final_data.head()

# description of the data
final_data.describe()

# checking duplicate rows
final_data.duplicated()

# information of the dataset
final_data.info()

"""# Exploratory Data Analysis (EDA)"""

# Visualizing the counts of different types transactions
plt.figure(figsize=(8,4))
sea.countplot(x='is_fraudulent', data=final_data, palette='BrBG')
plt.title('Fraudulent vs. Non-Fraudulent Transactions')
plt.xlabel('Is Fraudulent')
plt.ylabel('Count')
plt.xticks([0,1], ['Non-Fraudulent', 'Fraudulent'])
plt.show()

# Showing the distribution of the transactions
plt.figure(figsize=(10,6))
sea.histplot(final_data['amount'], bins=50, kde=True, color='green')
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
plt.show()

# Showing transactions by card type
plt.figure(figsize=(10,6))
sea.countplot(x='card_type', hue='is_fraudulent', data=final_data, palette='Set3')
plt.title('Fraudulent Transactions by Card Type')
plt.xlabel('Card Type')
plt.ylabel('Count')
plt.legend(title='Is Fraudulent', labels=['Non-Fraudulent', 'Fraudulent'])
plt.show()

# distribution of CLV
plt.figure(figsize=(10,6))
sea.histplot(final_data['CLV'], bins=50, kde=True, color='orange')
plt.title('Distribution of Customer Lifetime Value (CLV)')
plt.xlabel('CLV ($)')
plt.ylabel('Frequency')
plt.show()

# Evaluating the correlation matrix
corr_matrix = final_data[['amount', 'CLV', 'Customer_Age','Transaction_Frequency', 'is_fraudulent', 'Account_Tenure_Years']].corr()
# Plotting the heatmap
plt.figure(figsize=(8,6))
sea.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Filtering the fraudulent transactions
fraudulent_data = final_data[final_data['is_fraudulent'] == 1]
# Counting overall fraudulent transactions by the purchase category
fraud_counts = fraudulent_data['purchase_category'].value_counts()
# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(fraud_counts, labels=fraud_counts.index, autopct='%1.1f%%', startangle=140, colors=sea.color_palette('pastel'))
plt.title('Total Fraudulent Transactions by Purchase Category')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()

# Recognizing transactions by top 10 cities
top_cities = final_data['City'].value_counts().nlargest(10)
# Developing the horizontal bar chart
plt.figure(figsize=(12,6))
sea.barplot(y=top_cities.index, x=top_cities.values, palette='Set1')
# Adding titles and labels
plt.title('Total Transactions by Top 10 Cities')
plt.xlabel('Number of Transactions')
plt.ylabel('Cities')
# Showing the plot
plt.show()

# Generating a boxplot for Transaction_Frequency
plt.figure(figsize=(12, 6))
sea.boxplot(x='is_fraudulent', y='Transaction_Frequency', data=final_data, palette='Set2')
plt.title('Transaction Frequency by Fraudulent Transactions')
plt.xlabel('Is Fraudulent')
plt.ylabel('Transaction Frequency')
plt.xticks([0, 1], ['Non-Fraudulent', 'Fraudulent'])
plt.show()

