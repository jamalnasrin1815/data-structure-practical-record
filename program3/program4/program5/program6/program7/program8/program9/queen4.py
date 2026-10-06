# General N-Queens Problem

N = int(input("Enter the value of N: "))

board = [-1] * N
solutions = []

def is_safe(row, col):
    for i in range(row):

        # Same column
        if board[i] == col:
            return False

        # Same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(row):
    if row == N:
        solutions.append(board.copy())
        return

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1


solve(0)

print("\nTotal Solutions =", len(solutions))

for number, solution in enumerate(solutions, 1):
    print("\nSolution", number)

    for col in solution:
        print("." * col + "Q" + "." * (N - col - 1))