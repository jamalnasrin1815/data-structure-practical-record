SIZE = 5
queue = [None] * SIZE
front = -1
rear = -1

def enqueue(item):
    global front, rear

    if (rear + 1) % SIZE == front:
        print("Circular Queue is Full")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % SIZE
    queue[rear] = item
    print(item, "inserted")

enqueue(10)
enqueue(20)
enqueue(30)

print("Circular Queue:", queue)