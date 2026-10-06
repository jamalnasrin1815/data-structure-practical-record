queue = [10, 20, 30]

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print(queue.pop(0), "deleted from queue")

dequeue()
dequeue()

print("Queue:", queue)