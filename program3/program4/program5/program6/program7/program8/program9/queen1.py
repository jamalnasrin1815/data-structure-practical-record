# N-Queens using Backtracking

N = 4
board = [-1] * N
solutions = []

def is_safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False
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

print("All solutions for 4-Queens:")

for solution in solutions:
    for row in solution:
        print("." * row + "Q" + "." * (N - row - 1))
    print()