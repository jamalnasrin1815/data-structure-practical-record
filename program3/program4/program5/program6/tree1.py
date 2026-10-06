# Prim's Algorithm

graph = [
    [0, 2, 3, 0],
    [2, 0, 1, 4],
    [3, 1, 0, 5],
    [0, 4, 5, 0]
]

n = len(graph)
selected = [False] * n
selected[0] = True

print("Edges in Minimum Spanning Tree:")

total = 0

for _ in range(n - 1):
    minimum = 999
    x = y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "--", y, "=", minimum)
    total += minimum
    selected[y] = True

print("Minimum Cost =", total)