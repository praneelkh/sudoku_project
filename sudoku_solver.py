"""Project 2 - Sudoku Solver."""

def solve(board: list[list[int]]) -> bool:
    empty_space = find_empty(board)
    # If there are no empty spaces, the puzzle has been solved (base case)
    if not empty_space:
        return True
    # If there is an empty space...
    else: 
        (row, col) = empty_space
    for i in range(1, 10):
        # Check to see if any given number you choose is valid in that spot
        if valid(board, i, empty_space):
            # Place that number in the board
            board[row][col] = i
            # Try the new number until it fails
            if solve(board):
                return True
            # If it fails, replace the number with 0 and backtrack to repeat the process
            else:
                board[row][col] = 0
    return False

def valid(board: list[list[int]], num: int, position: tuple):
    #Check Row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False
    #Check Column
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False
    #Check Square
        box_col = position[1] // 3
        box_row = position[0] // 3
        for i in range(box_row*3, box_row*3 + 3):
            for j in range(box_col*3, box_col*3 + 3):
                if board[i][j] == num and position != (i,j):
                    return False
    return True
        

def print_board(board: list[list[int]]): 
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(f"| {board[i][j]}", end=" ")
            elif j == 8:
                print(f"{board[i][j]}")
            else:
                print(board[i][j], end=" ")
    return None

def find_empty(board: list[list[int]]):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                # (row, column)
                return (i, j)
    return None

sudoku_board = [
    [0, 0, 1, 0, 0, 0, 0, 0, 5],
    [0, 0, 7, 0, 0, 3, 0, 0, 0],
    [2, 0, 0, 9, 0, 0, 4, 1, 0],
    [1, 0, 0, 4, 0, 0, 2, 6, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 4, 0, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 8],
    [5, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 2, 0, 7, 0, 6, 5, 0]
]
solve(sudoku_board)
print_board(sudoku_board)