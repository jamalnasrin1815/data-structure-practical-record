stack = [10, 20, 30]

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print(stack.pop(), "popped from stack")

pop()
pop()

print("Stack:", stack)