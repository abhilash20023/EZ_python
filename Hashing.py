class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None and current.key != key:
            prev = current
            current = current.next
        if current is None:
            return None
        if prev is None:
            self.table[index] = current.next
        else:
            prev.next = current.next
        return current.value


ht = HashTable(10)
ht.insert(1, 'one')
ht.insert(11, 'eleven')
ht.insert(21, 'twenty-one')

print(ht.search(11))  
print(ht.search(11)) 