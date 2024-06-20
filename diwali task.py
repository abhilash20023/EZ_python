#!/usr/bin/env python
# coding: utf-8

# In[ ]:


hrs_trl=int(input("enter the hours to reach th venue"))
no_prb=int(input("enter the number of problems"))
remaining_hrs=4*60-hrs_trl

def calculateProblems(remaining_hrs,no_prb):
    solved_prob=0
    total_time=0
    for i in range(1,no_prb):
        time_used=5*i
        total_time+=time_used
        solved_prob+=1
        if time_used>remaining_hrs-total_time:
            break
    return solved_prob
print(calculateProblems(remaining_hrs,no_prb))


# In[ ]:




