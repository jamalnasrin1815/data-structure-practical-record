import heapq

heap = []

# Insertion
heapq.heappush(heap, 25)
heapq.heappush(heap, 15)
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print("Heap after insertion:", heap)

# Deletion
deleted = heapq.heappop(heap)

print("Deleted element:", deleted)
print("Heap after deletion:", heap)

# Insert another element
heapq.heappush(heap, 5)

print("Heap after inserting 5:", heap)