# Mobile Sales Dashboard Analysis

![DashBoard](Mobile_Sales_data\Mobile_Sales_DashBoard.png)

## Problem Statement
The objective of this project is to analyze mobile and tech accessory sales data to evaluate the performance of major smartphone brands. By analyzing metrics like units sold, unit prices, and customer ratings, the goal is to identify primary revenue drivers and understand brand market share to facilitate data-driven business decisions.

## Approach
- **Data Ingestion**: Analyzed transaction-level sales data containing 19,150 mobile sales records (`Mobile Sales Data.xlsx`) and an additional dataset for mobile tech accessories (`Mobile_Tech_Accessories.csv`).
- **Data Processing**: Calculated total revenue by multiplying `Units Sold` by `Price Per Unit`. 
- **Visualization**: A Power BI dashboard (`Mobile_sales_DashBoard.pbix`) was developed to aggregate these metrics visually and offer an interactive overview of market performance.
- **Metric Aggregation**: Grouped total unit sales and revenue by Brand to find the top performers and computed the average customer satisfaction ratings across all transactions.

## Key Performance Indicators (KPIs)
Based directly on the dataset analysis:
- **Total Revenue**: ₹769,204,988
- **Total Units Sold**: 19,150
- **Overall Average Customer Rating**: 3.69 / 5.0
- **Unique Brands Analyzed (Core Sales Data)**: 5 (Apple, Samsung, OnePlus, Vivo, Xiaomi)
- **Top Brand by Volume (Units Sold)**: Apple (3,932 units), closely followed by Samsung (3,923 units), OnePlus (3,830 units), Vivo (3,801 units), and Xiaomi (3,664 units).
