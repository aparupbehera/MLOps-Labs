# Lab 2: GCP Data Storage Warehouse Lab

##  Setup

### Step 1: Terminal Upload 

### Download csv file (Amazon_Sales_data.csv) from the dataset folder

1. Go to https://console.cloud.google.com
2. Create a new project on GCP. Get Project Id, say it's `project_id`
3. Create a bucket with name amazon-sales-bucket
4. Auth. login with gcloud on terminal.
5. Replace `project_id` with your actual GCP project ID in all queries.

**Verify data loaded:**
```sql
SELECT COUNT(*) FROM `project_id.amazon_sales_db.sales`;
```

On local system terminal, execute:
```bash
# Set your project
gcloud config set project project_id

# Create bucket and upload CSV
BUCKET_NAME="amazon-sales-bucket"
gsutil mb -l US gs://${BUCKET_NAME}/
gsutil mv Amazon_Sales_data.csv gs://${BUCKET_NAME}/
```

### Step 2: BigQuery Console

5. Go to https://console.cloud.google.com/bigquery
6. Click on **Add Data**. Upload csv file to BigQuery from the bucket created above. 
7. In the prompt create dataset name:`amazon_sales_db` and table name: `sales`
8. **Schema**: Auto detect
9. Click **CREATE TABLE**

---

## Go to the newly created table and Run queries

### 1. Sales Overview
```sql
SELECT 
    COUNT(DISTINCT `Order ID`) AS total_orders,
    SUM(`Units Sold`) AS total_units,
    ROUND(SUM(`Total Revenue`), 2) AS total_revenue,
    ROUND(SUM(`Total Profit`), 2) AS total_profit,
    ROUND((SUM(`Total Profit`) / SUM(`Total Revenue`)) * 100, 2) AS profit_margin_pct
FROM `project_id.amazon_sales_db.sales`;
```

### 2. Top Countries by Revenue
```sql
SELECT 
    Country,
    Region,
    COUNT(`Order ID`) AS total_orders,
    ROUND(SUM(`Total Revenue`), 2) AS revenue,
    ROUND(SUM(`Total Profit`), 2) AS profit
FROM `project_id.amazon_sales_db.sales`
GROUP BY Country, Region
ORDER BY revenue DESC
LIMIT 15;
```

### 3. Offline vs Online
```sql
SELECT 
    `Sales Channel`,
    COUNT(`Order ID`) AS orders,
    ROUND(SUM(`Total Revenue`), 2) AS revenue,
    ROUND(AVG(`Total Revenue`), 2) AS avg_order_value
FROM `project_id.amazon_sales_db.sales`
GROUP BY `Sales Channel`;
```

### 4. Customer Lifetime Value
```sql
SELECT 
    customer_id,
    customer_name,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(total_amount), 2) AS lifetime_value,
    ROUND(AVG(total_amount), 2) AS avg_order_value
FROM `project_id.amazon_sales_db.sales`
WHERE status = 'Delivered'
GROUP BY customer_id, customer_name
ORDER BY lifetime_value DESC
LIMIT 20;
```