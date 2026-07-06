#4.Count and display the total number of nodes in the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

head = Node(10)
head.ref = Node(20)
head.ref.ref = Node(30)
head.ref.ref.ref = Node(40)

count = 0
n = head

while n:
    count += 1
    n = n.ref

print("Total Nodes:", count)