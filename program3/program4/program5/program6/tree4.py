# Kruskal's Algorithm

edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]

edges.sort()

parent = [0, 1, 2, 3]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

total = 0

print("Edges in Minimum Spanning Tree:")

for weight, u, v in edges:
    if find(u) != find(v):
        print(u, "--", v, "=", weight)
        total += weight
        union(u, v)

print("Minimum Cost =", total)