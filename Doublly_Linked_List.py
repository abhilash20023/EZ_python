class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self, value):
        new_node=node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    def pop(self):
        if self.length==1:
            self.head=None
            self.tail=None
        if self.length==0:
            return None
        temp=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        temp.prev=None
        self.length-=1
        return temp.value
        
    def prepend(self,value):
        new_node=node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        temp=self.head
        self.head=new_node
        self.head.next=temp
        temp.prev=self.head
        # new_node.next=self.head
        # self.head.prev=new_node
        # self.head=new_node
        self.length+=1
        return True


    def pop_first(self):
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        temp=self.head
        self.head=self.head.next
        self.head.prev=None
        temp.next=None
        self.length-=1
        return temp
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set_value(self,index,value):
        # new_node=node(value)
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=node(value)
        before=self.get(index-1)
        after=before.next
        new_node.prev=before
        new_node.next=after
        before.next=new_node
        after.prev=new_node
        self.length+=1
        return True

    def remove(self,index):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length:
            return self.pop()
        temp=self.get(index)
        before=temp.prev
        after=temp.next
        before.next=after
        after.prev=before
        # temp.next=None
        # temp.prev=None
        self.length-1   
        return temp    

        
linkedlist=LinkedList(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.prepend(0)
# linkedlist.insert(1,0)
print(linkedlist.remove(0))
# print(linkedlist.get(2))
# linkedlist.set_value(1,5)
# linkedlist.pop_first()
# linkedlist.pop()
linkedlist.print_list() 
