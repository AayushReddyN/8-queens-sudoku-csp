def solve_sudoku_backtracking(board):
    def is_valid(num, row, col):
        # Check row
        for x in range(9):
            if board[row][x] == num:
                return False

        # Check column
        for x in range(9):
            if board[x][col] == num:
                return False

        # Check 3x3 subgrid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def find_empty_location(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return r, c
        return None, None

    row, col = find_empty_location(board)
    if row is None and col is None:
        return True  # Puzzle solved

    for num in range(1, 10):
        if is_valid(num, row, col):
            board[row][col] = num
            if solve_sudoku_backtracking(board):
                return True
            board[row][col] = 0  # Backtrack

    return False

def print_sudoku_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Example Sudoku Execution
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku_backtracking(sudoku_board)