#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Bubble Sort

L=list(map(int,input().split()))
n=len(L)
for j in range(0,n):
    for i in range(0,n-1-j):
        if L[i]>L[i+1]:
            L[i],L[i+1]=L[i+1],L[i]

print(L)


# In[5]:


#selection sort        
L=[9,7,5,8,10,26,44,3,1]
n=len(L)
min=L[0]
for j in range(0,n):
    pos=j
    min = L[j]
    for i in range(j,n):
        if L[i]<min:
            min=L[j]
            pos=i

        L[j],L[pos]=L[pos],L[j]
print(L)


# In[6]:


#bubble sort
l=[2,6,4,7,1,9]
n=len(l)
for j in range(0,n):
    ipfor i in range(0,n-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)


# In[7]:


def divide(l,low,high):
    j=low-1
    pi=high
    for i in range(low,high):
        if l[i]<l[pi]:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[pi],l[j]=l[j],l[pi]
    return j
def quick(l,low,high):
    if low<high:
        pi=divide(l,low,high)
        quick(l,low,pi-1)
        quick(l,pi+1,high)
    print(l)
l=[34,22,5,6,78,0,1]
quick(l,0,len(l)-1)
print(l)


# In[ ]:


#recursion  FAB Series
t=[0]

def fib(n):
    t[0]+=1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    n= int(input())
    print(fib(n))
    print(t)


# In[ ]:


#merge Sort


def merge(left,right):
    i=j=0
    temp=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
            
    while i<len(left):
        temp.append(left[i])
        i+=1
        
    while j<len(right):
        temp.append(right[j])
        j+=1

    return temp

def mergesort(L):
    if len(L) <= 1:
        return L
        
    mid = len(L)//2
    left=L[:mid] 
    right=L[mid:]
    
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    
    return merge(left_sorted,right_sorted)


if __name__=="__main__":
    L=list(map(int,input().split())) # 4 7 8 3 2 9 1 5
    sorted=mergesort(L)

    print("Sorted Array = ",sorted)

