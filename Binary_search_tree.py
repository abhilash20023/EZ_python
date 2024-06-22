# binary search tree
class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

def insert(root, value): 
    if root is None:
        return Node(value)  
    
    if value < root.value:
        root.left = insert(root.left, value)  
    else:
        root.right = insert(root.right, value)  

    return root 

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value,end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value,end=" ")
l = [4, 6, 7, 3, 8, 2, 5, 9, 1]
root = Node(l[0])
for i in l[1:]:
    root = insert(root, i)  
print("Inorder Traversal of the BST:")
inorder(root)
print("\npreorder Traversal of the BST:")
preorder(root)
print("\npostoder Traversal of the BST:")
postorder(root)