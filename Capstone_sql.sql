-- Transaction Fraud Analysis --

Use capstone; 
Go

Select * from financial_data
Select * from Merchant_details
Select * from location_details
Select * from Customer_Details
Select * from Card_Details

-- Developing an index on the customer_id and merchant_id within the financial_data table
CREATE INDEX idx_customer_merchant
ON financial_data (customer_id, merchant_id);

--Performing Analysis

-- 1. Calculating Average Transaction Amount per Merchant
   With AvgAmountPerMerchant as (
    Select merchant_id,AVG(amount) as Average_amount
    from financial_data
    group by merchant_id
)
select merchant_id, Average_amount
from AvgAmountPerMerchant
order by Average_amount desc;

-- 2. Retrieving top Cities with the Highest CLV (Customer Lifetime Value) for Fraudulent Transactions
select top 10 ld.City, AVG(fd.CLV) as Average_CLV
from financial_data fd
JOIN location_details ld on fd.location_ID = ld.location_ID
where fd.is_fraudulent = 1
group by ld.City
order by Average_CLV desc;

-- 3. Finding top Merchants with the Most Fraudulent Transactions 
select top 5 merchant_id, COUNT(*) as Fraudulent_Transaction_Count
from financial_data
where is_fraudulent = 1
group by merchant_id
order by fraudulent_transaction_count desc;

-- 4. Showing top 10 Customers by total Transaction Amount
select distinct top 10 
customer_id,
round(sum(amount) over (partition by customer_id), 2) as Total_Transaction_Amount
from financial_data
order by total_transaction_amount desc;

-- 5. Categorizing the transactions by amount  
select customer_id,
    count(*) as transaction_count,
    sum(amount) as total_amount,
    CASE 
        When sum(amount) < 100000 then 'Low Value'
		When sum(amount) between 100000 and 500000 then 'Medium Value'
        When sum(amount) > 500000 then 'High Value'
        ELSE 'Unknown'
    end as transaction_value_category
from financial_data
group by customer_id
order by total_amount desc;

-- 6. Customers with the transactions at Merchants related to "shopping" or "retail"
select distinct customer_id
from financial_data
where merchant_id IN (
    select merchant_id
    from merchant_details
    where purchase_category LIKE '%Shopping%' or purchase_category LIKE '%Retail%'
);

-- 7. Recognizing top Countries with the most fraudulent transactions
select ld.Country, 
count(fd.transaction_id) as fraud_count, 
round(SUM(fd.amount),2) as total_fraud_amount
from financial_data fd
JOIN location_details ld
ON fd.location_ID = ld.location_ID
where fd.is_fraudulent = 1
group by ld.Country
order by fraud_count desc;

---------------------------------------------------------------------------------------------------------------------











 




