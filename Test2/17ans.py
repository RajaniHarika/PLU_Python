#17.Create an undirected graph with the following edges:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("Adjacency List:")

for node in graph:
    print(node, "->", graph[node])