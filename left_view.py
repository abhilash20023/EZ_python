class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,Node,level) -> None:
        self.node=Node
        self.level=level
# def Left_View(root):
#     if root is None:
#         return

#     temp = node_data(root, 0)
#     Key_dic = {}
#     Q = [temp]

#     while Q:
#         cur = Q.pop(0)
        
#         if cur.level not in Key_dic:
#             Key_dic[cur.level] = cur.node.value

#         if cur.node.left is not None:
#             temp = node_data(cur.node.left, cur.level + 1)
#             Q.append(temp)

#         if cur.node.right is not None:
#             temp = node_data(cur.node.right, cur.level + 1)
#             Q.append(temp)

#     for i in sorted(Key_dic):
#         print(Key_dic[i])
    
#     print(Key_dic)
def Left_View(root):
    q=[root]
    q.append(None)
    print(root.value)
    while len(q)>0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                print(q[0].value)
                q.append(None)
        else:
            # print(curr.value,end=' ')
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)  
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
    Left_View(root)