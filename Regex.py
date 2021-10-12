#!/usr/bin/env python
# coding: utf-8

# #### Homework Regex

# In[1]:


import re
import ipytest
ipytest.autoconfig()


# In[2]:


speed = 'Speed limit sign says 90 km per hour. I thought it was for skateboards'
emails = 'luc_besson@example.com, daniel_morales@example.biz, emilien@example.net'
task4 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
task5 = 'Marseille is port city in the south of France, an important transit and trade center since its founding by the Greeks around 600 BC.'


# Задача 1:Вернуть первое слово из строки

# In[3]:


re.search(r'^\w+', speed)


# Задача 2: Вернуть первые 2 символа каждого слова

# In[4]:


re.findall(r'\b\w.', speed)


# Задача 3: Вернуть список доменов из списка адресов электронной почты. Доп.: вытащить только домен
# верхнего уровня

# In[5]:


re.findall(r'@\w+.\w+', emails)


# In[6]:


re.findall(r'@\w+.(\w+)', emails)


# Задача 4: Извлечь дату из строки ('Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'). 
# Доп.: вытащить только год

# In[7]:


re.findall('\d{2}-\d{2}-\d{4}', task4)


# Задача 5: Извлечь все слова, начинающиеся на гласную

# In[8]:


re.findall(r'\b[aeiouAEIOU]\w+', task5)


# Задача 6: Разбить строку по нескольким разделителям

# In[9]:


re.split(r'\W+', speed)







