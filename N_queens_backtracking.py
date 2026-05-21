def solve_n_queens_backtracking(n):
    board = [-1] * n  # board[i] will store the column of the queen in row i
    solutions = []

    def is_safe(row, col):
        # Check this column on upper rows
        for i in range(row):
            if board[i] == col:  # Same column
                return False
            if abs(board[i] - col) == abs(i - row):  # Same diagonal
                return False
        return True

    def backtrack(row):
        if row == n:
            # All queens are placed successfully
            solutions.append(list(board))
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack: remove queen

    backtrack(0)
    return solutions

def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = []
        for col in range(n):
            if solution[row] == col:
                line.append('Q')
            else:
                line.append('.')
        print(' '.join(line))
    print()

# Execution
N = 8
queens_solutions = solve_n_queens_backtracking(N)
print(f"Found {len(queens_solutions)} solutions.")