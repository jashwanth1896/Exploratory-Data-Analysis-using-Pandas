#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis (EDA) On Store Sales Data

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sd = pd.read_csv('train.csv')
sd


# In[3]:


sd.shape


# In[4]:


sd.head()


# In[5]:


# Finding duplicates if any
sd[sd.duplicated()]


# In[6]:


sd.duplicated().sum()


# In[7]:


# Finding null values 
sd[sd.isnull()]


# In[8]:


#Finding the column with null values
sd.isnull().sum()


# In[9]:


# Postal code column has null values
NVP=sd[sd['Postal Code'].isnull()]
NVP 


# In[10]:


NVP.shape


# In[11]:


# Burlington is the only city whose postal code is missing, so filling those null values with it s original postal code
sd['Postal Code']=sd['Postal Code'].fillna(5401)
sd['Postal Code']


# In[12]:


sd['Postal Code'].isnull().sum()


# In[13]:


# the null values are filled
sd.isnull().sum()


# In[14]:


sd.info()


# In[15]:


sd.head()


# In[16]:


sd['Order Date']=pd.to_datetime(sd['Order Date'],format= '%d/%m/%Y')
sd['Order Date']


# In[17]:


sd['Ship Date']=pd.to_datetime(sd['Ship Date'],format='%d/%m/%Y')
sd['Ship Date']


# In[18]:


# The data types of columns - "Order Date and Ship Date" are changed 
sd.info()


# In[19]:


sd['Order Date'].sort_values()


# In[38]:


sd.sort_values(by=['Order Date'],inplace = True)



# In[40]:


sd.reset_index(drop=True)


# In[22]:


sd['City'].value_counts()


# In[23]:


sd['Ship Mode'].value_counts()


# In[24]:


sd['Ship Mode'].value_counts().plot.pie()


# In[25]:


sd['Ship Mode'].value_counts().plot.bar()


# In[26]:


#Orders according to the segment
sd['Segment'].value_counts().plot.pie()


# In[27]:


sd['City'].value_counts()


# In[28]:


# Sale according to the state
sd['State'].value_counts()


# In[29]:


# Sales visualization according to the state
plt.figure(figsize=(20,8))
sd['State'].value_counts().plot.bar()


# In[30]:


# Top 10 states according to the sales 
top_state=sd.groupby(['State']).sum(numeric_only=True).sort_values('Sales',ascending=False)
top_state = top_state[['Sales']].round(2)
top_state


# In[ ]:





# In[31]:


top_state.reset_index(inplace=True)

ts=top_state.head(10)
ts


# In[151]:


#Visualizing top 10 state sales
plt.figure(figsize=(16,6))
plt.bar(ts['State'],ts['Sales'] ,color="red" , edgecolor='green')
plt.xticks(rotation='vertical')
plt.title('States With High Revenu ',fontsize=15)
plt.xlabel('State',fontsize=15)
plt.ylabel('Revenu',fontsize=15)

for k , v in ts['Sales'].items(): 
    if v > 200000 : 
        plt.text(k,v-100000,"$"+str(v),rotation=90,horizontalalignment='center')
    else:
        plt.text(k,v-50000,"$"+str(v),rotation=90,horizontalalignment='center')


# In[41]:


sd.head()


# In[50]:


top_city= sd.groupby(['City']).sum(numeric_only=True).sort_values('Sales',ascending=False)
top_city=top_city[['Sales']].round(2)
top_city.reset_index(inplace=True)
top_city


# In[54]:


tc= top_city.head(10)
tc


# In[57]:


# Visualizing the top 10 cities
plt.figure(figsize=(16,6))
plt.bar(tc['City'],tc['Sales'] ,color="#95dee3" , edgecolor='red')
plt.xticks(rotation='vertical')
plt.title('Cities With High Revenue',fontsize=15)
plt.xlabel('City',fontsize=15)
plt.ylabel('Revenue',fontsize=15)

for k , v in tc['Sales'].items(): 
    if v > 100000 : 
        plt.text(k,v-100000,"$"+str(v),rotation=90,horizontalalignment='center')
    else:
        plt.text(k,v-10000,"$"+str(v),rotation=90,horizontalalignment='center')


# In[61]:


# Top customers
top_customers = sd.groupby(['Customer Name']).sum(numeric_only=True).sort_values('Sales', ascending=False)
top_customers = top_customers[['Sales']].round(2)
top_customers.reset_index(inplace=True)
top_customers


# In[65]:


tcs = top_customers.head(10)
tcs


# In[68]:


# visualizing top 10 customers sales
plt.figure(figsize=(16,6))
plt.bar(tcs['Customer Name'],tcs['Sales'] ,color="red" , edgecolor='blue')
plt.xticks(rotation='vertical')
plt.title('States With High Revenu ',fontsize=15)
plt.xlabel('State',fontsize=15)
plt.ylabel('Revenu',fontsize=15)

for k , v in tcs['Sales'].items(): 
    if v > 100000 : 
        plt.text(k,v-100000,"$"+str(v),rotation=90,horizontalalignment='center')
    else:
        plt.text(k,v-10000,"$"+str(v),rotation=90,horizontalalignment='center')


# In[70]:


#Sales according to category
sd['Category'].value_counts()


# In[80]:


category_sales = sd.groupby(['Category']).sum(numeric_only=True).sort_values('Sales',ascending=False)
category_sales.reset_index(inplace=True)
category_sales


# In[83]:


# visualizing the top customers sales
plt.figure(figsize=(12,6))
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  (${v:d})'.format(p=pct,v=val)
    return my_autopct


plt.pie(category_sales['Sales'],labels=category_sales['Category'],autopct=make_autopct(category_sales['Sales']))


# In[86]:


#Top Products 
top_products = sd.groupby(['Product Name']).sum(numeric_only=True).sort_values('Sales',ascending=False).head(5)
top_products.reset_index(inplace=True)
top_products


# In[88]:


#Sales visualization in top 5 products
plt.figure(figsize=(15,10))
plt.pie(top_products['Sales'],labels=top_products['Product Name'],autopct=make_autopct(top_products['Sales']))


# In[91]:


#Extraction of date,month,year from the order date
sd['day']=sd['Order Date'].dt.day
sd['month']=sd['Order Date'].dt.month
sd['year']=sd['Order Date'].dt.year
sd.sample(5)


# In[93]:


# visualizing the year wise sales
sd['year'].value_counts().plot.pie()


# In[95]:


#Monthly wise sales
sd['month'].value_counts().plot.pie()


# In[104]:


# yearly sales
year_sales = sd.groupby(['year']).sum(numeric_only=True).sort_values('Sales',ascending=False)
year_sales.reset_index(inplace=True)
year_sales


# In[122]:


# visualize sales in each year 
plt.bar(year_sales['year'],year_sales['Sales'] ,color="purple" , edgecolor='blue')


# In[127]:


# sales in a separate year 2015
x = sd['year'] == 2015
df2 = sd[x]
sales = df2.groupby(['month']).sum(numeric_only=True).sort_values(['month'], ascending=True)
sales.reset_index(inplace=True)
sales


# In[129]:


#Visualizing sales for each month
plt.bar(sales['month'],sales['Sales'])


# In[134]:


# visualizing sales in each year with months and days details 
my_sales = sd.groupby([('year'),('month'),('day')]).sum(numeric_only=True)
my_sales.reset_index(inplace=True)
my_sales


# In[136]:


# drawing the sales as scatter to get the highest sales in each year  
plt.figure(figsize=(15,10))
plt.scatter(my_sales['year'],my_sales['Sales'])


# In[139]:


# get 2015 sales 
x = sd['year'] == 2015
df2 = sd[x]
sales = df2.groupby(['month']).sum(numeric_only=True)
sales.reset_index(inplace=True)
sales_2015 = [round(x,2) for x in list(sales['Sales'])]
sales_2015


# In[143]:


# get 2016 sales 
x = sd['year'] == 2016
df2 = sd[x]
sales = df2.groupby(['month']).sum(numeric_only=True)
sales.reset_index(inplace=True)
sales_2016 = [round(x,2) for x in list(sales['Sales'])]
sales_2016


# In[145]:


# get 2017 sales 
x = sd['year'] == 2017
df2 = sd[x]
sales = df2.groupby(['month']).sum(numeric_only=True)
sales.reset_index(inplace=True)
sales_2017 = [round(x,2) for x in list(sales['Sales'])]
sales_2017


# In[147]:


# get 2018 sales 
x = sd['year'] == 2018
df2 = sd[x]
sales = df2.groupby(['month']).sum(numeric_only=True)
sales.reset_index(inplace=True)
sales_2018 = [round(x,2) for x in list(sales['Sales'])]
sales_2018


# In[149]:


# drawing all the months in all the years in a good way so that we can see the differences between them 
import numpy as np


plt.figure(figsize=(15,8))

#day one, the age and speed of 13 cars:
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array(sales_2015)
plt.scatter(x, y , color = 'red')

#day two, the age and speed of 15 cars:
y = np.array(sales_2016)
plt.scatter(x, y , color = 'blue')



y = np.array(sales_2017)
plt.scatter(x, y , color = 'black')

y = np.array(sales_2018)
plt.scatter(x, y , color = 'green')

plt.show()


# In[150]:


# line plot
plt.figure(figsize=(15,8))

#day one, the age and speed of 13 cars:
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array(sales_2015)
plt.plot(x, y , color = 'red' ,label='2015')


#day two, the age and speed of 15 cars:
y = np.array(sales_2016)
plt.plot(x, y , color = 'blue' ,label='2016')



y = np.array(sales_2017)
plt.plot(x, y , color = 'black',label='2017')


y = np.array(sales_2018)
plt.plot(x, y , color = 'green' , label='2018')

plt.legend()
plt.show()

