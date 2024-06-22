class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def height(root):
    if root==None:
        return 0
    LH=height(root.left)
    RH=height(root.right)
    h=max(RH,LH)+1
    return h
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
    print()
    print(height(root))
    