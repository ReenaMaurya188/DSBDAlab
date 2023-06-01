
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv('facebook.csv')


# In[4]:


df.info


# In[5]:


df.shape


# In[6]:


df.sort


# In[7]:


df.sort()


# In[8]:


df.sort_values('Hour').head()


# In[9]:


pandas.dataframe.loc[]


# In[15]:


ages = df[["Hour","Paid"]]


# In[16]:


ages.head()


# In[18]:


row = df[df["Reach"] > 2000]


# In[19]:


row.head()


# In[20]:


adults = df.loc[df["Reach"] >20000 , "Month"]


# In[21]:


adults.head()


# In[22]:


array2 = np.arrange(8).reshape(2, 4)


# In[25]:


array2.display()


# In[26]:


array1 = np.arange(8)


# In[27]:


print("Original array : \n", array1)


# In[28]:


df.reshape()


# In[29]:


df.melt()


# In[30]:


df.transpose() ##row tp column and column to row


# In[31]:


numpy.reshape()


# In[32]:


df.reshape()


# In[33]:


df=pd.read_csv('facebook.csv')


# In[34]:


df1= pd.read_csv('facebook1.csv')


# In[36]:


concatenated = pd.concat([df, df1])


# In[37]:


concatenated = pd.concat([df, df1], axis="columns")


# In[38]:


concatenated.head()


# In[39]:


merge


# In[41]:


abc = pd.merge(df,df1)


# In[44]:


print(abc)

