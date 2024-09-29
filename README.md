# Transaction Fraud Analysis (Capstone Project)

# Overview

The Transaction Fraud Analysis Capstone Project focuses on identifying patterns of fraudulent transactions across various merchants, customers, and locations. This end-to-end analysis uses SQL, Python, and Power BI for data extraction, cleaning, analysis, and visualization. The project aims to uncover actionable insights regarding fraud patterns by analyzing transaction data, customer lifetime value (CLV), card types, and location-based trends.

# Dataset Details

_Main Dataset link:_ https://www.kaggle.com/datasets/isabbaggin/transaction-fraudulent-financial-syntheticdata

The project involves multiple datasets covering different aspects of the financial transactions. These datasets are:

- financial_data: Contains information about transaction amounts, CLV (Customer Lifetime Value), fraud indicators, and transaction frequency.
- merchant_details: Provides information on merchants, including the purchase category and merchant IDs.
- location_details: Stores details about the geographical location of the transactions, including city and country.
- customer_details: Contains customer-specific information such as age, account tenure, and customer ID.
- card_details: Provides card-related information such as card type and card IDs.

Each dataset was imported and merged into a single comprehensive DataFrame for analysis.

# SQL Analysis

In the first phase, I utilized SQL to perform preliminary analysis and data extraction. Key queries included:

- _Indexing:_ Developed indexes on customer_id and merchant_id within the financial_data table to improve query performance.
- _Average Transaction Amount per Merchant:_ Calculated the average transaction value per merchant to identify high-value merchants.
- _Top Cities with the Highest CLV for Fraudulent Transactions:_ Identified the top cities with the highest average CLV for fraudulent transactions to focus fraud prevention measures.
- _Top Merchants with the Most Fraudulent Transactions:_ Listed the top 5 merchants with the highest count of fraudulent transactions to pinpoint vulnerable business segments.
- _Top 10 Customers by Total Transaction Amount:_ Highlighted the top 10 customers based on their total transaction amount to understand high-value customer behavior.
- _Categorizing Transactions by Amount:_ Segregated transactions into "Low", "Medium", and "High" value categories to provide better customer segmentation.
- _Transactions Related to Shopping or Retail:_ Identified customers who transacted with merchants from shopping or retail sectors, which are typically more prone to fraud.
- _Top Countries with the Most Fraudulent Transactions:_ Showed the countries where fraudulent transactions are most prevalent.

# Python Analysis

Using Python, I imported, merged, and cleaned the data using pandas and performed exploratory data analysis (EDA) with matplotlib and seaborn. Key steps and visualizations included:

**_Data Merging and Cleaning:_**

Merged all the datasets (financial, customer, merchant, location, and card data) to create a consolidated DataFrame.
Dropped irrelevant columns and handled missing values.

**_Exploratory Data Analysis (EDA):_**

- _Fraudulent vs Non-Fraudulent Transactions:_ A bar chart comparing the count of fraudulent and non-fraudulent transactions provided a clear view of the distribution.

- _Distribution of Transaction Amounts:_ Visualized using a histogram, this provided insights into the spread of transaction values, highlighting the occurrence of high-value transactions.

- _Fraudulent Transactions by Card Type:_ A count plot showed how different card types are linked to fraudulent transactions, revealing vulnerabilities related to specific card types.

- _Customer Lifetime Value (CLV) Distribution:_ A histogram of CLV values helped analyze customer loyalty and spending power.

- _Correlation Heatmap:_ Showed the correlations between key variables like amount, CLV, transaction frequency, and fraudulent transactions to identify potential relationships.

- _Fraudulent Transactions by Purchase Category:_ A pie chart depicted the percentage of fraudulent transactions across different purchase categories, highlighting sectors more prone to fraud.

- _Top 10 Cities by Transaction Count:_ A bar chart displaying the cities with the highest number of transactions, helping focus on regions with high transaction volumes.

- _Transaction Frequency by Fraudulent Transactions:_ A box plot to compare transaction frequencies between fraudulent and non-fraudulent transactions, helping understand buying behavior linked to fraud.

# Power BI Analysis and Insights

The third phase involved using Power BI to create interactive and dynamic dashboards for advanced analysis and reporting. Key visualizations and insights are:

**1. Customers by Transaction Frequency Category:**

A bar chart visualized the distribution of customers across different transaction frequency categories, providing insight into their purchasing patterns. This helps to tailor marketing strategies based on transaction frequency.

**2. Fraudulent Transactions by Country:**

A bar chart compared fraudulent transactions by country. It was found that Germany had the highest number of fraudulent transactions, focusing prevention efforts in specific regions.

**3. Fraudulent Transactions by Age Category:**

A pie chart illustrated the distribution of fraudulent transactions by age group. Younger customers were identified as the group with the highest number of fraudulent activities, followed by middle-aged customers.

**4. Fraud Amount by Transaction Frequency Category:**

A bar chart visualizing the total fraudulent amount for each transaction frequency category revealed that customers with high transaction frequencies had the highest fraudulent transaction amounts, marking them as a high-risk group.

**Interactive Filters:**

Users can filter by city, card type, and purchase category to dynamically explore the dashboard, providing flexibility in uncovering specific insights across different segments.

# Key Insights:

- Fraudulent Activity by Age: Younger and middle-aged customers are more prone to fraudulent activities.
- Geographical Fraud Distribution: Germany had the highest number of fraudulent transactions among the countries analyzed.
- High-Risk Customers: Customers with high transaction frequency not only spend more but are also at higher risk of conducting fraudulent transactions.
- Purchase Category Fraud: Certain purchase categories, such as "Shopping" and "Retail", were found to have more frequent fraudulent transactions.

# Conclusion

This capstone project demonstrates the comprehensive approach taken to analyze transaction fraud across multiple dimensions. SQL was used to extract and pre-analyze the data, Python facilitated deeper exploratory analysis, and Power BI provided powerful interactive dashboards. The findings will help organizations focus on specific regions, demographics, and business segments for better fraud prevention strategies.
