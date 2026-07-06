#19.Perform a Breadth-First Search (BFS) traversal starting from vertex A.
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = []
queue = deque(["A"])

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for i in graph[node]:
            queue.append(i)