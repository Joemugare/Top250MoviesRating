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


# #  Select relevant numeric columns for correlation analysis

# In[57]:


numeric_columns = ['rating', 'budget', 'box_office']
numeric_data = df[numeric_columns]


# # Calculate the correlation matrix

# In[58]:


correlation_matrix = numeric_data.corr()


# # Create a correlation heatmap

# In[59]:


plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Movie Attributes')
plt.show()


# In[ ]:




