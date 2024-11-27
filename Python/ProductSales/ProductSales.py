#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset alt. the path
df = pd.read_csv(r"C:\electronic_product_sales.csv.zip")

# Inspect the dataset
print(df.shape)  # Dimensions of the dataset
print(df.sample(10))  # Sample rows to observe the structure
print(df.info())  # Data types and missing values
print(df.describe())  # Summary statistics

# Check for missing values
print(df.isnull().sum())


# In[2]:


# Create boxplots to observe outliers
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Boxplot for 'Quantity Ordered'
sns.boxplot(y=df['Quantity Ordered'], ax=axes[0])
axes[0].set_title('Boxplot of Quantity Ordered')

# Boxplot for 'Price Each'
sns.boxplot(y=df['Price Each'], ax=axes[1])
axes[1].set_title('Boxplot of Price Each')

# Display the plots
plt.show()


# In[4]:


# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Verify the data type conversion
print(df.info())


# In[5]:


# Add a new column for total sales
df['Total Sales'] = df['Quantity Ordered'] * df['Price Each']

# Display the updated dataset
print(df.head())


# In[6]:


# Calculate the average price for each product
average_price_per_product = df.groupby('Product')['Price Each'].mean()

# Sort and display the top 10 most expensive products
top_10_expensive_products = average_price_per_product.sort_values(ascending=False).head(10)
print(top_10_expensive_products)


# In[7]:


# Sum total sales by product
total_sales_per_product = df.groupby('Product')['Total Sales'].sum()

# Sort and display the top 10 products by sales
top_10_products_by_sales = total_sales_per_product.sort_values(ascending=False).head(10)
print(top_10_products_by_sales)


# In[9]:


# Extract month and year from 'Order Date'
df['Month'] = df['Order Date'].dt.month
# Group by 'Month' and sum the 'Total Sales'
monthly_sales = df.groupby('Month')['Total Sales'].sum().reset_index()
monthly_sales


# In[10]:


# Plotting the monthly sales using Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=monthly_sales, x='Month', y='Total Sales', palette='viridis')

# Adding titles and labels
plt.title('Monthly Sales Progression')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)  # Rotate month labels for better readability
plt.tight_layout()

# Show the plot
plt.show()


# In[11]:


# Filter the DataFrame for months 4 (April), 10 (October), and 12 (December)
filtered_df = df[df['Month'].isin([4, 10, 12])]
# Extract the day of the week from 'Order Date'
filtered_df['Day of Week'] = filtered_df['Order Date'].dt.day_name()

# Calculate total sales if not already done
filtered_df['Total Sales'] = filtered_df['Quantity Ordered'] * filtered_df['Price Each']

# Group by 'Day of Week' and sum the 'Total Sales'
sales_by_day = filtered_df.groupby('Day of Week')['Total Sales'].sum()

# Reorder the days of the week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales_by_day = sales_by_day.reindex(days_order)
sales_by_day

# Reorder the days of the week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales_by_day = sales_by_day.reindex(days_order)

# Plotting the sales by day of the week using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_day.index, y=sales_by_day.values, palette='viridis')

# Adding titles and labels
plt.title('Total Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)  # Rotate day labels for better readability
plt.tight_layout()

# Show the plot
plt.show()


# In[16]:


# Extract the hour from 'Order Date'
df['Hour'] = df['Order Date'].dt.hour
# Calculate total sales if not already done
df['Total Sales'] = df['Quantity Ordered'] * df['Price Each']
# Group by 'Hour' and sum the 'Total Sales'
sales_by_hour = df.groupby('Hour')['Total Sales'].count()
sales_by_hour

# Plotting the sales by hour using Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x=sales_by_hour.index, y=sales_by_hour.values, palette='viridis')

# Adding titles and labels
plt.title('Total Sales by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Nr of Sales')
plt.xticks(rotation=45)  # Rotate hour labels for better readability
plt.tight_layout()

# Show the plot
plt.show()


# In[21]:


# Define a function to categorize hours into time ranges
def categorize_time(hour):
    if 23 <= hour or hour <= 7:
        return 'Night Owl'
    elif 8 <= hour <= 10:
        return 'Morning Bird'
    elif 11 <= hour <= 15:
        return 'Noon Crawler'
    elif 16 <= hour <= 22:
        return 'Evening Bug'

# Apply the function to create a new column 'Time Range'
df['Time Range'] = df['Hour'].apply(categorize_time)
df.head()

# Count the number of sales for each time range
sales_count_by_time_range = df['Time Range'].value_counts()
# Plotting the pie chart using Matplotlib with Seaborn styling
plt.figure(figsize=(8, 8))
sns.set_style("whitegrid")  # Apply Seaborn theme for better aesthetics
plt.pie(sales_count_by_time_range, labels=sales_count_by_time_range.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(sales_count_by_time_range)))

# Adding a title
plt.title('Sales Distribution by Time Range')

# Show the plot
plt.show()


# In[22]:


df['Product'].unique()
# Define a function to categorize products
def categorize_product(product_name):
    if 'laptop' in product_name.lower():
        return 'Laptop'
    elif 'phone' in product_name.lower():
        return 'Phone'
    else:
        return 'Other'

# Apply the function to create a new column 'Category'
df['Category'] = df['Product'].apply(categorize_product)
df.head()
# Group by 'Month' and 'Category' and sum the 'Total Sales'
monthly_sales_by_category = df[~(df['Category']=='Other')].groupby(['Month', 'Category'])['Total Sales'].sum().unstack()

# Plotting the dual bar plot using Seaborn
plt.figure(figsize=(12, 6))
monthly_sales_by_category.plot(kind='bar', stacked=False, colormap='viridis', width=0.8)

# Adding titles and labels
plt.title('Monthly Sales for Laptops vs Phones')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)  # Rotate month labels for better readability
plt.legend(title='Category')
plt.tight_layout()

# Show the plot
plt.show()


# In[23]:


# Define a function to split the string and return the second element
def extract_city(address):
    parts = address.split(',')
    if len(parts) > 1:
        return parts[1].strip()  # Strip to remove any leading/trailing whitespace
    else:
        return np.nan

# Apply the function to create a new column 'City'
df['City'] = df['Purchase Address'].apply(extract_city)
df['City'].unique()

sales_by_city = df.groupby('City')['Total Sales'].sum()

# Sort the cities by total sales in descending order
top_cities = sales_by_city.sort_values(ascending=False)
# Plotting the bar plot
plt.figure(figsize=(8, 6))
top_cities.plot(kind='bar', color='skyblue')

# Adding titles and labels
plt.title('Top 3 Cities with Most Sales')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)  # Rotate city labels for better readability

# Show the plot
plt.show()


# In[24]:


# Filter the DataFrame for the specified cities
cities_of_interest = ['New York City', 'San Francisco', 'Los Angeles']
filtered_df = df[df['City'].isin(cities_of_interest)]
# Group by 'Product' and sum the 'Total Sales'
sales_by_product = filtered_df.groupby('Product')['Total Sales'].sum()
# Find the product with the most sales
top_product = sales_by_product.idxmax()
top_sales = sales_by_product.max()

# Display the product with the most sales
print(f"The product with the most sales in {', '.join(cities_of_interest)} is '{top_product}' with total sales of {top_sales}.")


# In[ ]:




