class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

class node_data:
    def __init__(self,Node,Hkey) -> None:
        self.node=Node
        self.Hkey=Hkey
def Top_View(root):
    temp=node_data(root,0)
    Key_dic={}
    Q=[temp]
    Q.append(None)
    while len(Q)!=0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                Q.append(None)
        else:
            if cur.Hkey not in Key_dic.keys():
                Key_dic[cur.Hkey]=cur.node.value
            if cur.node.left!=None:
                temp=node_data(cur.node.left,cur.Hkey-1)
                Q.append(temp)
            if cur.node.right!=None:
                temp=node_data(cur.node.right,cur.Hkey+1)
                Q.append(temp)
    for i in sorted(Key_dic):
        print(Key_dic[i])
    
    print(Key_dic)

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
    # levelorder(root)
    Top_View(root)
    
