#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df= pd.read_csv(r"C:\Users\acer\Downloads\archive\business.retailsales.csv")
df1= pd.read_csv(r"C:\Users\acer\Downloads\archive\business.retailsales2.csv")


# # Data cleaning( Category wise Sales(Table1))

# In[6]:


df


# In[7]:


df.info()


# In[5]:


df.dropna(inplace= True)


# In[6]:


df.info()


# In[8]:


df["Discounts"]=df['Discounts'].abs()


# In[9]:


df["Returns"]=df['Returns'].abs()


# In[10]:


df["Total Net Sales"]=df['Total Net Sales'].abs()


# In[11]:


df["Net Quantity"]=df['Net Quantity'].abs()


# In[12]:


df


# In[13]:


df2=df.groupby("Product Type").sum()


# In[14]:


df2


# In[15]:


df2=df2.reset_index()


# In[16]:


df2


# ## 

# In[17]:


df.describe()


# # Data cleaning( year wise sales(Table1))

# In[18]:


df1


# In[19]:


df1["Discounts"]=df1["Discounts"].abs()


# In[20]:


df1["Returns"]=df1["Returns"].abs()


# In[21]:


df1


# In[22]:


sales_by_year= df1.groupby("Year").sum(['Total Orders', 'Gross Sales', 'Discounts', 'Returns', 'Net Sales', 'Shipping', 'Total Sales'])


# In[23]:


sales_by_year


# In[157]:


sales_by_year.reset_index(inplace= True)
sales_by_year


# In[24]:


average_sales= df1.groupby("Year").mean(['Total Orders' , 'Gross Sales', 'Discounts', 'Returns', 'Net Sales', 'Shipping', 'Total Sales'])


# In[25]:


average_sales


# # EXPLANATORY DATA ANALYSIS

# In[26]:


qty_sold_by_category=df2[["Product Type", "Net Quantity"]]
qty_sold_by_category


# In[53]:


qty_sold_by_category


# In[77]:


qty_sold_by_category.plot(kind="pie", y="Net Quantity",figsize=(10,6), legend=False, title= "Qty sold category wise");


# In[78]:


Total_sales_category_wise=df2[["Product Type", "Total Net Sales"]]
Total_sales_category_wise


# In[131]:


sns.barplot(x="Product Type", y="Total Net Sales", data=Total_sales_category_wise).set(title="Total sales category wise($)")
plt.xticks(rotation= 90);


# In[132]:


Discount=df2[["Product Type", "Discounts"  ]]
Discount.set_index("Product Type", inplace= True)
Discount


# In[151]:


Discount.plot(kind="barh", xlabel="Discounts", ylabel="Product Type", title=" Discount($)", legend= False, figsize=(10,7));


# In[125]:


product_returned=df2[["Product Type", "Returns"]]
product_returned.reset_index()
product_returned


# In[129]:


sns.barplot(x="Product Type", y="Returns", data=product_returned ).set(title="Product returned($)")
plt.xticks(rotation= 90);


# In[160]:


annual_sales=sales_by_year[["Year", "Total Sales"]]


# In[165]:


annual_sales.plot(kind="line", x="Year", y="Total Sales", title="Annual Sales", legend= False);


# In[150]:


sns.barplot(x="Year", y="Total Orders", data= sales_by_year).set(title="Quantity sold");


# # CONCLUSION

# Baskets and Art&Sculptures are the most sold items of the business which generates most of the revenue,
# whereas Easter and Gift baskets are the least sold products of the business.
# 
# The annual sales of the business is growing every year at certain rate without showing any diminishing values.  
# 

# In[ ]:




