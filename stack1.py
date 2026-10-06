stack = []

def push(item):
    stack.append(item)
    print(item, "pushed into stack")

push(10)
push(20)
push(30)

print("Stack:", stack)