class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def evaluate(root):
    # If leaf node, return its value
    if root.left is None and root.right is None:
        return int(root.data)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.data == '+':
        return left + right
    elif root.data == '-':
        return left - right
    elif root.data == '*':
        return left * right
    elif root.data == '/':
        return left / right


# Construct expression tree
root = Node('*')

root.left = Node('+')
root.right = Node('4')

root.left.left = Node('2')
root.left.right = Node('3')

print("Expression: (2 + 3) * 4")
print("Result:", evaluate(root))