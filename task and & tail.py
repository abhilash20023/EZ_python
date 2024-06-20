#!/usr/bin/env python
# coding: utf-8

# In[1]:


moves=int(input("enter the number of step"))
moves_of=[]
count=0
sum1=0
for i in range(0,moves):
    a=int(input())
    moves_of.append(a)
for i in moves_of:
    sum1=sum1+i
    if sum1==0:
        count=count+1
print(count)


# In[ ]:




