import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Step 2: Calculate the total sales for each product
df['Total_Sales'] = df['Quantity'] * df['Price']

# Step 3: Group data by product and calculate total sales and quantity sold
product_sales = df.groupby('Product').agg({'Total_Sales': 'sum', 'Quantity': 'sum'}).reset_index()

# Step 4: Print out the product sales summary
print("Product Sales Summary:")
print(product_sales)

# Step 5: Create a bar plot for the total sales of each product
plt.figure(figsize=(8, 5))
plt.bar(product_sales['Product'], product_sales['Total_Sales'], color='lightblue')
plt.title('Total Sales by Product', fontsize=16)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: Create a line plot for total sales over time (by Date)
sales_by_date = df.groupby('Date')['Total_Sales'].sum().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(sales_by_date['Date'], sales_by_date['Total_Sales'], marker='o', color='green')
plt.title('Total Sales Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

