#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://mainacademy.ua/'> <img src='https://mainacademy.ua/wp-content/uploads/2019/03/logo-main.png' alt = 'Хмм, щось з інтернетом'/></a>
# ___
# 
# # Module 6: Basics of data visualization

# ## Lab work 6
# 
# 

# #### Мета: 
# 
# * навчитися візуалізовувати дані в Python

# ### Завдання:

# In[182]:


import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn as sns


# In[183]:


np.random.seed(0)

df = pd.DataFrame(data={'a':np.random.randint(0, 100, 30),
                        'b':np.random.randint(0, 100, 30),
                        'c':np.random.randint(0, 100, 30)})
df.head()


# Створити візуалізацію, аналогічно рисунку 
#  - перші 3 графіки візуалізувати, викорстовуючи значення із df
#  - останній це пряма пропорційність

# In[184]:



fig, ax = plt.subplots(2,2,figsize = (15,8))

sns.lineplot(data = df['a'], ax = ax[0,0])
sns.lineplot(data = df['b'], ax = ax[0,1])
sns.lineplot(data = df['c'], ax = ax[1,0])
sns.lineplot(data = np.arange(0, 30), ax = ax[1,1])


# картинка с примером с задания
# ![image.png](attachment:image.png)

# Створити візуалізацію, аналогічно рисунку 

# In[79]:


plt.figure(figsize = (15,8))
sns.lineplot(data = df['a'])


# картинка с примером с задания
# ![image.png](attachment:image.png)

# Створити візуалізацію, аналогічно рисунку 
# - використовуйте колонки `a` та `b`

# In[90]:


fig, ax = plt.subplots(2,1, figsize = (15,8))
sns.lineplot(data = df['a'], ax = ax[0])
sns.lineplot(data = df['b'], ax = ax[1])


# картинка с примером с задания
# ![image.png](attachment:image.png)

# In[ ]:





# Створити візуалізацію, аналогічно рисунку 
# - використовуйте колонки `a` та `b`

# In[126]:


plt.figure(figsize = (15,8))
ax = sns.lineplot(data = df[['a', 'b']],  legend = False)
ax.lines[1].set_linestyle("-")


# картинка с примером с задания
# ![image.png](attachment:image.png)

# Створити візуалізацію, аналогічно рисунку 
# - використовуйте колонки `a` та `b`
# - задайте стиль 'darkgrid' за допомогою команди `sns.set_style`

# In[18]:


plt.figure(figsize=(15,8))
sns.set_style("darkgrid")
sns.lineplot(data = df[['a', 'b']], legend = False)

# fig, ax = plt.subplots(figsize=(15,8))
# ax.plot(df[['a', 'b']])


# In[7]:


# пример с задания 


# In[ ]:





# Створити візуалізацію, аналогічно рисунку 
# - для колонки `a` використайте червоний колір та лінію формату `-.`
# 
# - для колонки `b` використайте помаранчевий колір та товщину `10`
# 
# - для колонки `c` використайте жовтий колір та товщину `1` і маркер `o`
# 

# In[14]:


plt.figure(figsize=(15,8))
sns.set_style('darkgrid')
plt.plot(df[['a']], 'r-.')
plt.plot(df[['b']], 'orange', linewidth = 10)
plt.plot(df[['c']], 'yellow', linewidth = 1, marker = 'o')


# In[15]:





# Створити візуалізацію, аналогічно рисунку 
# - і не забудьте про легенду :)

# In[ ]:





# In[181]:


fig, ax = plt.subplots(3, 1, figsize = (15,8))
plt.tight_layout()
ax[0].plot(df['a'])
ax[0].legend(["Line A"], loc = 'lower right') 

ax[1].plot(df['b'])
ax[1].legend(['Line B'], loc = 'center left')

ax[2].plot(df['c'])


# картинка с примером с задания
# ![image.png](attachment:image.png)

# In[ ]:





# Створити візуалізацію, аналогічно рисунку 
# - використайте томатний колір та відстань між стовбцями 0.5

# In[144]:


plt.figure(figsize = (15, 8))
plt.bar(df.index, df['a'], color = ('salmon')) # не смогла подобрать именно тот оттенок, что в задании
plt.legend('a')


# In[10]:


# пример с задания


# Створити візуалізацію, аналогічно рисунку 
# - добавте всі підписи та правильний маркер

# In[175]:


plt.figure(figsize=(20,8))
plt.plot(df['a'], marker = '^')
plt.title('This is the Title', fontsize = 13)
plt.xlabel('This is the X Axis', fontsize = 20)
plt.ylabel('This is the Y Axis')


# In[ ]:





# In[12]:


#пример с задания


# In[ ]:




