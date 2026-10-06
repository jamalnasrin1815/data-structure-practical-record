stack = [10, 20, 30]

def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element =", stack[-1])

peek()