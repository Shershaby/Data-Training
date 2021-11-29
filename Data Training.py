#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

data = pd.read_csv(r'F:\AI Diploma\New\exercise\AB_NYC_2019.csv')
data.head()


# In[5]:


data.tail()


# In[7]:


data.info()


# In[10]:


data.describe()


# In[12]:


titanic_data = pd.read_csv(r'F:\AI Diploma\New\exercise\Titanic_train.csv')
titanic_data.head()


# In[13]:


titanic_data.info()


# In[14]:


titanic_data.describe()


# In[18]:


import matplotlib.pyplot as plt
titanic_data.hist(bins=30, figsize=(20,15))
plt.show()


# In[28]:


plt.scatter(titanic_data['Survived'], titanic_data['Age'])
plt.xlabel('Pclass')
plt.ylabel('Age')
plt.show()


# In[2]:


import numpy as np
array_1 = np.array([[1, 2, 7], [3, 4, 8]])
array_2 = np.array([[1, 2], [3, 9], [4, 16]])
np.dot(array_1, array_2)

