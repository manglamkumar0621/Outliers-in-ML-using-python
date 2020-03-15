#!/usr/bin/env python
# coding: utf-8

# # Identify Outliers
# Outliers are data point that lies outside the dataset.

# # Criteria to identify the outliers
#     1.Data point falls outside of 1.5 times of an interquartile range above 3rd quartile and below 1st quartile
#     2.Data point falls outside of 3 standard deviations. In case of z-score, if z-score falls outside of 2 standard deviation.

# # Reasons for existance of outliers
#     1. Variability in data
#     2. error in measurement

# # Ways to find outliers
#     1. Using scatter plot
#     2. Box plot
#     3. Using z-score
#     4. Using the IQR (interquarentile range)

# # 1.Using scatter plot
# ![](dg_scatter_plot.png)

# # 2.Using box plot
# ![](box_plot.png)

# # 3.Using z-score
#     Ref: https://www.math.ubc.ca/~pwalls/math-python/jupyter/latex/
#     Formula: z-score = (Observation - mean)/standard deviation
# $$z = \frac{(X_i - \mu)}{\sigma}$$
# 

# In[2]:


import numpy as np


# In[44]:


np.random.seed(13)
dataset = np.random.randint(900,1000,100)
dataset = np.append(np.array([1,2,3,6]),dataset)


# # Finding the Outliers
# 
# 

# In[46]:


outliers = []
def find_outliers(data):
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)
    
    for n in data:
        z_score = (n-mean)/std
        #print(n,z_score,sep=':')
        if np.abs(z_score) > threshold:
            outliers.append(n)
    return outliers
    


# In[47]:


#dataset = np.array([2,25,26,27,28,29,34,35])
find_outliers(dataset)


# # 4. Interquartile range
# 75% - 25% values in dataset
# Steps involved:
#     1. Sort the dataset in increasing order.
#     2. Calculate 1st and 3rd quartile.
#     3. Find interquartile range: iqr = q3-q1
#     4. Find lower bound = q1 - (iqr*1.5)
#     5. Find upper bound = q2 + (iqr*1.5)
#     
#     Anything that lies outside the lower and upper bound range is OUTLIER.

# In[48]:


#Sorting the dataset
sorted(dataset)


# In[57]:


#Calculate 1st and 3rd quartile
q1,q3 = np.percentile(dataset,[25,75])
q1,q3


# In[59]:


#Find interquartile range
iqr = q3-q1
iqr


# In[64]:


low_bound_value = q1 - (iqr*1.5)
upp_bound_value = q3 + (iqr*1.5)
low_bound_value,upp_bound_value
# Anything outside the low_bound_value and upp_bound_value range is Outliers.

