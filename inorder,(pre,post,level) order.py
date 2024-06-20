#!/usr/bin/env python
# coding: utf-8

# In[6]:


class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def preorder(root):
    if root== None:
        return
    
    print(root.value)
    preorder(root.left)
    preorder(root.right)
    
if __name__=="__main__":
    root=node(1)
    
    root.left=node(2)
    root.right=node(3)
    
    root.left.left=node(4)
    root.left.right=node(5)
    
    root.right.left=node(6)
    root.right.right=node(7)
    
    preorder(root)


# In[15]:


class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def postorder(root):
    if root== None:
        return
    
    
    postorder(root.left)
    postorder(root.right)
    print(root.value)
  
    
if __name__=="__main__":
    root=node(1)
    
    root.left=node(2)
    root.right=node(3)
    
    root.left.left=node(4)
    root.left.right=node(5)
    
    root.right.left=node(6)
    root.right.right=node(7)
    
    postorder(root)


# In[14]:


class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def inorder(root):
    if root== None:
        return
    
    
    inorder(root.left)
    print(root.value)
    inorder(root.right)
  
    
if __name__=="__main__":
    root=node(1)
    
    root.left=node(2)
    root.right=node(3)
    
    root.left.left=node(4)
    root.left.right=node(5)
    
    root.right.left=node(6)
    root.right.right=node(7)
    
    inorder(root)


# In[22]:


#level
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def Level_order(root):
    Q=[root]
    Q.append(None)
    
    while len(Q)>0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(cur.value,end=' ')
            if cur.left!=None:
                Q.append(cur.left)
            if cur.right!=None:
                Q.append(cur.right)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(8)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    print('BFS\nLevel order Traversal')
    Level_order(root)


# In[25]:


class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def leaf_nodes(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        print(root.value, end=" ")
    
    leaf_nodes(root.left)
    leaf_nodes(root.right)


if __name__=="__main__":
    root=node(1)

    root.left=node(2)
    root.right=node(3)

    root.left.left=node(4)
    root.left.right=node(5)

    root.right.left=node(6)
    root.right.right=node(7)

    root.left.right.left=node(9)
    root.left.right.right=node(10)

    root.right.right.right=node(11)

    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    leaf_nodes(root)


# In[ ]:





# In[ ]:





# In[ ]:




