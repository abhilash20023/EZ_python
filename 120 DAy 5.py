#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


def is_valid_exp(exp):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in exp:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or brackets[char] != stack.pop():
                return False
    
    return len(stack) == 0

def main():
    while True:
        exp = input("Enter an expression (or 'q' to quit): ")
        if exp.lower() == 'q':
            break
        
        if is_valid_exp(exp):
            print(f"The expression '{exp}' is valid.")
        else:
            print(f"The expression '{exp}' is NOT valid.")

if __name__ == "__main__":
    main()


# In[1]:


def find_next_largest_right(arr):
    n = len(arr)
    result = [-1] * n  
    
    stack = [] 
    
    for i in range(n - 1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result


arr = [3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
output = find_next_largest_right(arr)
print(output)  


# In[4]:


class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
Head=Tail=Node(10)
Tail.next=Node(20)
Tail=Tail.next
Tail.next=Node(30)
Tail=Tail.next
Tail.next=Node(40)
Tail=Tail.next
def display(Head):
    if Head.value==None:
        print('Linked List is empty')
    curr=Head
    while curr!=None:
        print(curr.value,end=' ')
        curr=curr.next
    print()
display(Head)
def Add_front(Head,data):
    temp=Node(data)
    temp.next=Head
    Head=temp
    return Head
Head=Add_front(Head,20)
display(Head)
def Add_End(Tail,data):
    temp=Node(data)
    Tail.next=temp
    Tail=temp
Add_End(Tail,60)
display(Head)
def Specified_Position(Head,pos,data):
    cur=Head
    temp=Node(data)
    while cur!=None:
        if pos==cur.value:
            temp.next=cur.next
            cur.next=temp
            break
        else:
            cur=cur.next
Specified_Position(Head,20,22)
display(Head)


# In[ ]:




