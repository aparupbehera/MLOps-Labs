# Amazon Sales Dataset Overview

The **Amazon Sales Dataset** is a comprehensive dataset for sales and supply chain analysis, frequently used for business intelligence, data analytics, and visualization tasks. It contains **100+ transaction records** across multiple regions, countries, and product categories spanning from **2010 to 2017**.

---

## Features

Each sales record has **fourteen distinct attributes**:

### Geographic & Business Context
• **Region** (STRING): Geographic region (e.g., Asia, Europe, Sub-Saharan Africa, Australia and Oceania)  
• **Country** (STRING): Specific country where the sale occurred  
• **Sales Channel** (STRING): Distribution method - Online or Offline  
• **Order Priority** (STRING): Priority level - H (High), M (Medium), L (Low), C (Critical)

### Product Information
• **Item Type** (STRING): Product category (Baby Food, Cereal, Office Supplies, Fruits, Vegetables, Household, Personal Care, Clothes, Cosmetics, Beverages, etc.)

### Order Details
• **Order ID** (INTEGER): Unique identifier for each order  
• **Order Date** (DATE): Date when the order was placed  
• **Ship Date** (DATE): Date when the order was shipped

### Quantity & Pricing
• **Units Sold** (INTEGER): Number of units sold in the order  
• **Unit Price** (FLOAT): Selling price per unit in USD  
• **Unit Cost** (FLOAT): Cost per unit in USD

### Financial Metrics
• **Total Revenue** (FLOAT): Total revenue generated (Units Sold × Unit Price)  
• **Total Cost** (FLOAT): Total cost incurred (Units Sold × Unit Cost)  
• **Total Profit** (FLOAT): Profit earned (Total Revenue - Total Cost)

---

## Dataset Statistics

• **Total Records**: 100+ transactions  
• **Date Range**: May 2010 - January 2017  
• **Regions Covered**: 5 major geographic regions  
• **Countries**: 50+ countries worldwide  
• **Product Categories**: 12 distinct item types  
• **Sales Channels**: Online and Offline  

---

## Use Cases

This dataset is ideal for:

• **Exploratory Data Analysis (EDA)**: Understanding sales patterns, trends, and distributions  
• **Business Intelligence**: Revenue analysis, profit margins, regional performance  
• **Time Series Analysis**: Seasonal trends, year-over-year growth