# Kruskal's Algorithm

edges = [
    (2, 1, 2),
    (3, 0, 2),
    (1, 1, 2),
    (4, 1, 3),
    (5, 2, 3),
    (2, 0, 1)
]

edges.sort()

parent = [0, 1, 2, 3]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

print("Edges in MST:")

total = 0
count = 0

for weight, u, v in edges:
    if find(u) != find(v):
        print(u, "--", v, "=", weight)
        total += weight
        union(u, v)
        count += 1

        if count == 3:
            break

print("Minimum Cost =", total)