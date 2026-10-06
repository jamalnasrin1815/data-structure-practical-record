queue = []

def enqueue(item):
    queue.append(item)
    print(item, "inserted into queue")

enqueue(10)
enqueue(20)
enqueue(30)

print("Queue:", queue)