#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # Read the CSV file into a pandas DataFrame

# In[53]:


df = pd.read_csv('IMDB Top 250 Movies.csv')


# In[54]:


df


# In[55]:


pd.set_option('display.max_rows',250)


# # show the whole data set

# In[56]:


df.head(250)


# # Select relevant columns for analysis

# In[60]:


columns_of_interest = ['genre', 'rating', 'budget']


# # Filter data for movies with valid ratings and budgets

# In[61]:


filtered_data = df[df['rating'].notnull() & df['budget'].notnull()]


# # Create a histogram to visualize the distribution of ratings

# In[62]:


plt.figure(figsize=(8, 6))
plt.hist(filtered_data['rating'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Ratings')
plt.show()


# # Create a violin plot to compare rating distributions by genre

# In[64]:


plt.figure(figsize=(12, 8))
sns.violinplot(x='genre', y='rating', data=filtered_data, palette='Set2', inner='quartile')
plt.xlabel('Genre')
plt.ylabel('Rating')
plt.title('Distribution of Movie Ratings by Genre')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[ ]:




