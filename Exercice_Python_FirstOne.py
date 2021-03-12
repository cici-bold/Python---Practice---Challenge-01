#!/usr/bin/env python
# coding: utf-8


# In[4]:


f = open('unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
print(names_list[0:10])



# In[8]:


names_data = []

for name in names_list:
    comma_list = name.split(',')
    names_data.append(comma_list)
    
print(names_data[0:5])



# In[10]:


numerical_list = []

for line in names_data:
    name = line[0]
    count = float(line[1])
    new_list = [name, count]
    numerical_list.append(new_list)
    
print(numerical_list[0:5])



# In[11]:


final_list = []

for line in numerical_list :
    name = line[0]
    population = line[1]
    if population >= 1000:
        final_list.append(name)
        
print(final_list[0:10])

