# N-Queens using Backtracking

N = 6
board = [-1] * N
count = 0

def is_safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve(row):
    global count

    if row == N:
        count += 1

        print("Solution", count)
        for i in range(N):
            print("." * board[i] + "Q" +
                  "." * (N - board[i] - 1))
        print()
        return

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1

solve(0)

print("Total Solutions =", count)