from Node import Node
from LinkedList import LinkedList

n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)

list = LinkedList(n1, n3)

print(list.search(3).__dict__)