class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(HL, H, data):
    new_node = Node(data)
    if not HL[H]:
        HL[H] = new_node
        return
    curr = HL[H]
    while curr.next:
        curr = curr.next
    curr.next = new_node


def search(HL, key):
    H = key % 10
    current = HL[H]
    while current:
        if current.data == key:
            return True
        current = current.next
    return False


def delete_node(HL, key):
    H = key % 10
    current = HL[H]
    prev = None
    if current and current.data == key:
        HL[H] = current.next
        return
    while current and current.data != key:
        prev = current
        current = current.next
    if not current:
        return
    prev.next = current.next


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
def print_hashlist(hashList):
    for i in hashList:
        if i is None:
            print("Empty",end=" ")
        else:
            print_list(i)
        
k = [20, 30, 45, 25, 67]
hashList = [None for _ in range(10)]
for i in k:
    H = i % 10
    insert(hashList, H, i)

print_hashlist(hashList)

k = [22,10,47,56,100,50,92,99,79]#if n>10 use k%n
hashList = [False for _ in range(10)]
for e in k:
    for j in range(len(k)):
        x=((e%10)+j)%10
        if hashList[x]==False:
            hashList[x]=e
            break

print(hashList)
print("\n" ,search(hashList, 25))
print( search(hashList, 99))


delete_node(hashList, 30)
delete_node(hashList, 67)

print_hashlist(hashList)