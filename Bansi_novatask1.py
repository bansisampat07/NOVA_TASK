#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


data = pd.read_csv('D:/Bansi/SE/EDSTASK1.csv')


# In[3]:


data['start_datetime'] = pd.to_datetime(data['start.date'].astype(str) + ' ' + data['start.time'])


# In[4]:


data.head()


# In[102]:


data.columns = data.columns.str.replace('.','_')


# In[101]:


data.head()


# In[13]:


data['end_datetime'] = pd.to_datetime(data['start_date'].astype(str) + ' ' + data['end'])


# In[103]:


data.info()


# In[90]:


plt.hist(data['duration_s'], bins = 30)
plt.xlabel('Flare Duration (seconds)')
plt.ylabel('No of flares')
plt.title('Distribution of Flare Durations')
plt.show()


# The above histogram shows the frequeny of flare duration of the given data. It is seen that the no of flares decrease as the duration increases. Which means most of the flares recorded have a smaller duration(in the range of 0-1000sec).

# In[105]:


data['start_datetime'].hist(bins=365)
plt.xlabel('Start Date')
plt.ylabel('Number of Flares')
plt.title('Flare Frequency Over Time')
plt.show()


# The above histogram shows no of flares that were recorded over 14 years, from 2002 to 2016.

# In[41]:


energy_counts = data['energy_kev'].value_counts()
sns.barplot(x=energy_counts.index, y=energy_counts.values)
plt.title('Histogram of Energy Bands')
plt.xlabel('Energy Band (keV)')
plt.ylabel('Number of Flares')
plt.xticks(rotation=45)

plt.tight_layout()



# The above graph shows the energy range in which the flares are emitted.

# In[100]:


colors = ['3-6','6-12','12-25','25-50','50-100','100-300','300-800','800-7000','7000-20000']
#size = data['energy_kev'][0:1000].value_counts()
sns.scatterplot(x=data['duration_s'][0:1000], y=data['total_counts'][0:1000],
                        hue=data['energy_kev'], hue_order = colors, palette = 'Spectral')
plt.yscale('log')
plt.xscale('linear')
plt.tight_layout()


# In[76]:


data.info()


# In[ ]:




