class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.height=1
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.value,end=" ")
    inorder(root.right)

def insert(root,super):
    if not root:
        return node(super)
    if super<root.value:
        root.left=insert(root.left,super)
    else:
        root.right=insert(root.right,super)
       
if __name__=="__main__":
    vl=[19.99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i)
    inorder(root)