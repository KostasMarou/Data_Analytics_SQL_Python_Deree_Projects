#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load libraries and mount Google Drive (if applicable)
import pandas as pd

# Load the CSV file // change the path
df = pd.read_csv(r"C:\vgsales.csv")

# Display the first 5 rows
df.head()

# Get the shape of the dataset
df.shape

# Summary statistics of the dataset
df.describe()

# Information about data types and missing values
df.info()


# In[2]:


# Drop rows with missing values
df = df.dropna()

# Verify the dataset after cleaning
df.info()


# In[3]:


# Sort values by Global_Sales in descending order and select the top record
highest_sales_game = df.sort_values('Global_Sales', ascending=False).head(1)
print(highest_sales_game)


# In[4]:


# Get unique platforms in the dataset
unique_platforms = df['Platform'].unique()
print(unique_platforms)


# In[5]:


# Filter for PS4 games and sort by Global_Sales
ps4_top10 = df[df['Platform'] == 'PS4'].sort_values('Global_Sales', ascending=False).head(10)
print(ps4_top10)

# Add a combined sales column for Europe and Japan
df['eu_jp_sales'] = df['EU_Sales'] + df['JP_Sales']

# Top 10 PS4 games by EU + JP sales
ps4_top10_eu_jp = df[df['Platform'] == 'PS4'].sort_values('eu_jp_sales', ascending=False).head(10)
print(ps4_top10_eu_jp)


# In[13]:


# Filter for XOne games released in 2016
xbox_2016 = df[(df['Platform'] == 'XOne') & (df['Year'] == 2016)]

# Top-selling XOne game in Europe in 2016
top_eu_sales = xbox_2016.sort_values('EU_Sales', ascending=False)
print(top_eu_sales)


# In[7]:


# Replace 'XOne' with 'X Box One'
df['Platform'].replace('XOne', 'X Box One', inplace=True)

# Verify the replacement
df.tail(30)


# In[8]:


# Filter PC games with Global_Sales > 3
pc_high_sales = df[(df['Platform'] == 'PC') & (df['Global_Sales'] > 3)]

# Count the number of such games
print(len(pc_high_sales))

# Display the games
print(pc_high_sales)


# In[14]:


# Filter for Action games
action_games = df[df['Genre'] == 'Action']

# Find the Action game with the highest global sales
top_action_game = action_games.sort_values('Global_Sales', ascending=False)
print(top_action_game)


# In[16]:


# Count games by year and sort in descending order
games_by_year = df.groupby('Year').count().sort_values(['Name'], ascending=False)
print(games_by_year)

# Bar plot for the count of games by year
df.groupby('Year').count()['Name'].plot.bar(figsize=(18,6))
None


# In[17]:


# Filter for games released in 2009
df_2009 = df[df['Year'] == 2009]

# Count games by platform in 2009
platform_2009 = df_2009.groupby('Platform').count().sort_values(['Name'], ascending=False)
print(platform_2009)


# In[18]:


# Sum global sales by platform and sort in descending order
top_5_platforms = df.groupby('Platform').sum().sort_values('Global_Sales', ascending=False).head(5)

# Bar plot for the top 5 platforms
top_5_platforms['Global_Sales'].plot.bar(rot=45)


# In[19]:


# Sum EU sales by publisher and sort in descending order
top_3_publishers = df.groupby('Publisher').sum().sort_values('EU_Sales', ascending=False).head(3)

# Pie plot for the top 3 publishers by EU sales
top_3_publishers['EU_Sales'].plot.pie(figsize=(8, 8))

# Compare with Global Sales using a pie plot
top_3_publishers['Global_Sales'].plot.pie(figsize=(8, 8))


# In[21]:


# Count games by genre
top_genres = df.groupby('Genre').count().sort_values(['Name'], ascending=False).head(5)

# Bar plot for top genres
top_genres['Name'].plot.bar(rot=45)

# Filter by year and compare genres
df_2014 = df[df['Year'] == 2014]
df_2014.head()

top_genres_2014 = df_2014.groupby('Genre').count().sort_values(['Name'], ascending = False).head()
top_genres_2014

top_genres_2014['Name'].plot.bar(rot = 45)

for year in [2014, 2015, 2016]:
    print(f"\nTop genres in {year}:")
    df_year = df[df['Year'] == year]
    top_genres_year = df_year.groupby('Genre').count().sort_values('Name', ascending=False).head()
    print(top_genres_year)
    top_genres_year['Name'].plot.bar(rot=45, title=f"Top Genres in {year}")


# In[22]:


top_genres['Name'].plot.bar(rot=45)


# In[23]:


top_genres_2014['Name'].plot.bar(rot = 45)


# In[ ]:




