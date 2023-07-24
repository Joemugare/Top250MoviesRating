#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# # Read the CSV file into a pandas DataFrame

# In[11]:


df = pd.read_csv('IMDB Top 250 Movies.csv')


# In[24]:


df


# In[25]:


pd.set_option('display.max_rows',250)


# # show the whole data set

# In[26]:


df.head(250)


# # Sort the DataFrame by the "rating" column in descending order

# In[27]:


df_sorted_by_rating = df.sort_values(by='rating', ascending=False)


# # Select the top 20 highest-rated movies

# In[34]:


top_20_movies = df_sorted_by_rating.head(20)


# In[35]:


top_20_movies


# # Create a bar chart to visualize the top 20 highest-rated movies

# In[37]:


plt.figure(figsize=(12, 8))
plt.bar(top_20_movies['name'], top_20_movies['rating'], color='purple')
plt.xlabel('Movie Name')
plt.ylabel('Rating')
plt.title('Top 20 Highest-Rated Movies')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[ ]:




