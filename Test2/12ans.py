# 12.Display all the elements of the queue in FIFO order
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Queue Elements:")

while queue:
    print(queue.popleft(), end=" ")
