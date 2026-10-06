# Adjacency List

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

print("Adjacency List:")

for vertex in graph:
    print(vertex, ":", graph[vertex])