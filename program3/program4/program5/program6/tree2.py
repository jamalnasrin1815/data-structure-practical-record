import heapq

graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 1), (3, 4)],
    2: [(0, 3), (1, 1), (3, 5)],
    3: [(1, 4), (2, 5)]
}

visited = set()
heap = [(0, 0, -1)]
total = 0

print("Edges in MST:")

while heap:
    weight, vertex, parent = heapq.heappop(heap)

    if vertex in visited:
        continue

    visited.add(vertex)

    if parent != -1:
        print(parent, "--", vertex, "=", weight)
        total += weight

    for neighbour, edge_weight in graph[vertex]:
        if neighbour not in visited:
            heapq.heappush(heap, (edge_weight, neighbour, vertex))

print("Minimum Cost =", total)