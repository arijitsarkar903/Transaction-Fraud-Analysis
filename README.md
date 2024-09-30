# Transaction Fraud Analysis (Capstone Project)

# Overview

The Transaction Fraud Analysis Capstone Project focuses on detecting and analyzing fraudulent transactions across merchants, customers, and locations. A structured methodology was applied, utilizing SQL for data extraction and normalization, Python for exploratory data analysis (EDA), and Power BI for dynamic visualization. The project aims to highlight fraudulent patterns, offering insights into customer behavior and high-risk areas.

# Objectives

The primary objectives of this project are:

- To identify patterns of fraudulent transactions.
- To normalize and organize raw data into structured datasets.
- To analyze key variables such as transaction amount, CLV (Customer Lifetime Value), and fraud indicators.
- To develop interactive dashboards for fraud detection and reporting.

# Dataset Details

_Main Dataset link:_ https://www.kaggle.com/datasets/isabbaggin/transaction-fraudulent-financial-syntheticdata

The project involves multiple datasets covering different aspects of the financial transactions. These datasets are:

- financial_data: Contains information about transaction amounts, CLV (Customer Lifetime Value), fraud indicators, and transaction frequency.
- merchant_details: Provides information on merchants, including the purchase category and merchant IDs.
- location_details: Stores details about the geographical location of the transactions, including city and country.
- customer_details: Contains customer-specific information such as age, account tenure, and customer ID.
- card_details: Provides card-related information such as card type and card IDs.

Each dataset was imported and merged into a single comprehensive DataFrame for analysis.

# Methods
The project follows a comprehensive workflow split into three main phases:

**Data Normalization and SQL Processing:**

- Initially, raw data was imported, and normalization procedures were implemented to organize the dataset into multiple smaller datasets, each representing different entities (e.g., customer details, merchant information, transaction details).
- SQL was used to store and manage these datasets. Several queries were applied for data preprocessing, indexing, and basic analysis. Key tasks included:
- Creating indexes on customer_id and merchant_id for query optimization.
- Identifying the top merchants with fraudulent transactions and categorizing transactions based on their value.
- Exporting the clean, structured datasets to be used in the next phase.

**Python Analysis and Data Exploration:**

- The normalized datasets were directly imported into Python from the SQL local server. The data was merged, cleaned, and prepared for exploratory data analysis (EDA) using Python’s libraries such as pandas, matplotlib, and seaborn.

_Key tasks included:_

- Handling missing values and irrelevant columns to ensure clean datasets.
- Conducting detailed EDA, including visualizations such as histograms, bar charts, and heatmaps, to uncover relationships between variables like transaction frequency, CLV, and fraudulent behavior.
- Analyzing correlations between key variables to establish patterns of fraudulent activity.

**Power BI Dashboard for Reporting:**

- After data exploration, insights were transformed into an interactive dashboard using Power BI for comprehensive reporting. Power BI allowed for dynamic filtering and visualization, enabling users to explore fraud trends across regions, age groups, and transaction categories.
- The dashboard included:
- Visuals such as bar charts, pie charts, and interactive maps to display the distribution of fraudulent transactions.
- Filters based on city, card type, and merchant category to allow users to tailor their analysis dynamically.
- A focus on highlighting high-risk customers, regions, and age groups prone to fraudulent activities.

# Conclusion

This project demonstrates the effective use of SQL, Python, and Power BI in analyzing transaction fraud. The structured methodology allowed for a comprehensive understanding of fraudulent patterns, providing a basis for identifying high-risk customer segments and regions. This approach can be leveraged for enhanced fraud detection and prevention across various financial institutions.
