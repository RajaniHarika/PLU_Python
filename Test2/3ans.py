#3.Delete the node containing 30 from the linked list and display the updated
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

head = Node(10)
head.ref = Node(20)
head.ref.ref = Node(30)
head.ref.ref.ref = Node(40)

n = head
while n.ref:
    if n.ref.data == 30:
        n.ref = n.ref.ref
        break
    n = n.ref

n = head
while n:
    print(n.data, end=" -> ")
    n = n.ref
print("None")
