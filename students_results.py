#!/usr/bin/env python
# coding: utf-8

# In[1]:


## importing libraries

import numpy as np
import pandas as pd


# In[2]:


# list of students and rollno importing as dataframe df1
df1=pd.DataFrame({"names":['vineet','hisham','raj','ajeet','sujit','ramesh','priya','priyanka','suresh','ritesh','hitesh','jatin','chitesh','suman','raman','aman','ravi','shravi','chavvi','himanshu'],"rno":['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']})
df1


# In[3]:


# results and rollno data importing as dataframe df2
df2=pd.DataFrame({"results":['fail','fail','pass','pass','fail','pass','fail','pass','pass','pass','pass','fail','fail','fail','pass','fail','pass','fail','pass','pass'],"rno":['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']})
df2


# In[5]:


# merging the data df1 and df2 into df3 on rollno
df3=pd.merge(df1,df2)
df3


# In[6]:


# seeing top rows data 
df3.head()


# In[24]:


# to count total no of records in data 
df3.count()


# In[8]:


# filtering passed students
passed_stu = df3[df3["results"] == "pass"]
passed_stu


# In[9]:


# filtering failed students 
failed_stu = df3[df3["results"] == "fail"]
failed_stu


# In[11]:


# count of passed students
passed_students=passed_stu.count()
passed_students


# In[21]:


# count of passed students
df4=len(df3[df3["results"]=="pass"])
df4


# In[20]:


# count of failed stud
failed_students=failed_stu.count()
failed_students


# In[22]:


# count of failed students
df5=len(df3[df3["results"]=="fail"])
df5


# In[7]:


# sorting the data by names in Ascending order
df3.sort_values('names')


# In[ ]:





# In[ ]:




