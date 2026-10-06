import heapq

heap = [10, 20, 30, 40, 50]
heapq.heapify(heap)

print("Original Heap:", heap)

deleted = heapq.heappop(heap)

print("Deleted element:", deleted)
print("Heap after deletion:", heap)