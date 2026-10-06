import heapq

heap = []

# Insert elements
heapq.heappush(heap, -10)
heapq.heappush(heap, -20)
heapq.heappush(heap, -5)
heapq.heappush(heap, -30)

# Convert negative values back
max_heap = [-x for x in heap]

print("Max Heap:", max_heap)