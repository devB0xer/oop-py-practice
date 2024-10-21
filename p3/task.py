from Node import Node
from LinkedList import LinkedList

n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)

# init
list = LinkedList(n1, n3)

# len
print(list.len())

# search
print(list.search(3).__dict__)

#append
n4 = Node(4)
list.append(n4)
print(list.len(), list.search(4).data)

#remove
list.remove(2)

print(list.len())

