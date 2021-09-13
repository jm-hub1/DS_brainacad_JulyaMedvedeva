#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://mainacademy.ua/'> <img src='https://mainacademy.ua/wp-content/uploads/2019/03/logo-main.png' alt = 'Хмм, щось з інтернетом'/></a>
# ___
# 
# # Module 5: Data analysis with NumPy and Pandas

# ## Lab work 5.2
# 
# 

# #### Мета: 
# 
# * навчитися працювати із бібліотекою Pandas в Python.

# ### Завдання:

# In[35]:


import pandas as pd


# Вивести версію та конфігурацію бібліотеки:

# In[8]:


pd.__version__


# In[46]:


df = pd.read_csv('Ecommerce Purchases.csv')
df.head()


# Скільки рядків і стовпців в наборі даних:

# In[36]:


f'рядків  - {df.shape[0]}, стовпців - {df.shape[1]}'


# Перевірити, чи в наборі даних містяться порожні значення:

# In[38]:


# способ 1
df.isnull().sum()


# In[229]:


# способ 2
df.info()


# Яка середня ціна закупки (Purchase Price):

# In[101]:


df.columns


# In[103]:


df['Purchase Price'].mean()


# Скільки людей користуються англійською мовою "en" на веб-сайті:

# In[123]:


df.loc[df['Language'] == 'en']['Language'].count()


# Скільки людей має посаду «Lawyer»?

# In[124]:


df.loc[df['Job'] == 'Lawyer']['Job'].count()


# Скільки людей зробило покупку вранці та скільки людей зробило покупку після обіду?

# In[125]:


df.groupby(df['AM or PM'])['AM or PM'].count()


# In[132]:


df[df['CC Security Code'] == df['CC Security Code'].min()]


# Які 5 найпоширеніших назв вакансій?

# In[146]:


df.Job.value_counts().head()


# Хтось здійснив покупку, яка надійшла від Lot: "90 Wt", та якою була ціна придбання для цієї транзакції?

# In[167]:


# ПРИМечание: Условие с задания  Lot: "90 Wt" НЕ находится:
df[df['Lot'] == '90 Wt']


# In[173]:


# Перебирала ручками и нашла, что есть похожий лот, но с дпохожими буква, поэтому я искала по лоту = 'WT' (ОБЕ буквы заглавные).
df[df['Lot'] == '90 WT']


# In[176]:


# ПРИМечание: под заданием "кто осуществил" буду понимать, что нужно вывести название комании.
df[df['Lot'] == '90 WT'][['Lot', 'Company', 'Purchase Price']]


# Яка електронна адреса особи з таким номером кредитної картки: 4926535242672853 ?

# In[189]:


df[df['Credit Card'] == 4926535242672853][['Email']]


# Скільки людей використовує American Express  і здійснили покупку на суму понад 100 доларів?

# In[208]:


df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 100)].agg({'CC Provider' : 'count'})
# ПРИМечание: НЕТ таких людей. Таблица ниже показывает, что нет покупок выше 100 дол.


# In[275]:


df[(df['CC Provider'] == 'American Express')].sort_values(by = 'Purchase Price', ascending = False).head()


# In[226]:


# ПРИМечание: Что б показать какие то данные , я изменила усвлоия на диапазон суммы плкупки - between(90,100)
df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'].between(90,100))].agg({'CC Provider' : 'count'})


# In[198]:


df.groupby(df['CC Provider'] == 'American Express')


# Скільки людей мають кредитну картку, термін дії якої закінчується в 2025 році?

# In[265]:


# создала колонку, где прописан только год. 
df['CC Exp Year'] = df['CC Exp Date'].apply(lambda x: x.split('/')[1])


# In[266]:


# количество людей с окончанием дейсвия карты в 2025 году.
df.loc[df['CC Exp Year'] == '25'].shape[0]


# In[ ]:





# Які найкращі 5 найпопулярніших постачальників / хостів електронної пошти (наприклад, gmail.com, yahoo.com тощо ...).

# In[315]:


# сделала колонку, где указаны только названия хостингов. 
df['Email_hosting'] = df['Email'].apply(lambda x: str(x.split('@')[1]))


# In[314]:


# сделала промежуточный DF, содержащий нужные данные.
tem_df = df.groupby(df['Email_hosting']).agg({'Email_hosting' : 'count'})                    .rename(columns = {'Email_hosting' : 'Email_hosting_count'})

# в промежуточном DF отсоритирвала данные и выбрала первые 5.
tem_df.sort_values(by = 'Email_hosting_count', ascending = False).head()


# Виведіть зведену таблицю по браузерах(Browser Info), посаді(Job), та кількості транзакцій :

# In[329]:


df_check = df.pivot_table(index = ['Browser Info', 'Job'] , values = 'Purchase Price', aggfunc = 'count' )
# проверка df_check.sort_values(by = 'Purchase Price', ascending = False)


# In[ ]:





# Створіть нову колонку "Actual price", яка утворюється із "Purchase Price" та націнки за принципом:
# - якщо "Purchase Price" > 50, націнка 20%
# - якщо "Purchase Price" > 100, націнка 10%
# - в інших випадках націнка 30%
#    

# In[34]:


def prise_group(price):
    if 50 <= price < 100 :
        new_price = price * 1.2
    if price >= 100:
        new_price = price * 1.1
    else:
        new_price = price * 1.3
    return new_price
        

df['Actual price'] = df['Purchase Price'].apply(prise_group)
df[['Purchase Price', 'Actual price']].head() #для проверки


# In[ ]:





# Зробіть рангування набору даних по "Language" та "Actual price" в порядку спадання ціни.
# 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rank.html

# In[62]:


df['Language_r'] = df['Language'].rank()
df['Actual price_r'] = df['Actual price'].rank()
df[['Actual price', 'Actual price_r', 'Language', 'Language_r']].sort_values(by = 'Actual price_r', ascending = False).head(20)


# In[ ]:





# Колонку "Language" (категоріальна змінна) "закодуйте", тобто утворити індикаторні колоник. В наборі не повинна залишитися колонка "Language".
# 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rank.html

# In[44]:





# In[29]:


# делала через "класс".
class OHE():
    def fit_transform(self, df, column_name, drop = False):
        df['temp'] = 1 # нужно вводить. если values на основании строки, то в таблице на пересечении будут эти названия вместо 1
        transform = pd.pivot(df, columns = column_name, values = 'temp').fillna(0) #изменёная таблица.
        df_with_join = df.join(transform, how = 'left').drop('temp', axis = 1) #джоин изменённой таблицы. 
                                                                               # и удаление временной колонки 'temp'

        if drop == True:
            wo_column_df = df_with_join.drop([column_name], axis = 1)
            return wo_column_df
        else:
            return df_with_join


# In[48]:


df1 = OHE()


# In[49]:


df_final = df1.fit_transform(df, 'Language', drop = True)


# In[50]:


df_final.head()


# In[ ]:





# Кінцевий набір даних збережіть у файл з розширенням csv.

# In[59]:


df_final.to_csv('Lab work 5.2 final file.csv', index = False)


# In[ ]:




