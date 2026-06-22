import pandas as pd
df = pd.read_excel('Mobile_Sales_data/Mobile Sales Data.xlsx')
df['Total Sales'] = df['Units Sold'] * df['Price Per Unit']
print(f"Total Revenue: {df['Total Sales'].sum()}")
print(f"Total Units Sold: {df['Units Sold'].sum()}")
print(f"Unique Brands: {df['Brand'].nunique()}")
print(f"Avg Rating: {df['Customer Ratings'].mean():.2f}")
print("Top Brands by Units Sold:")
print(df.groupby('Brand')['Units Sold'].sum().sort_values(ascending=False).head(5))
