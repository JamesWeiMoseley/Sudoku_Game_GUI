
N = 9           # size of the rows and columns

# this is the main function. First it will check if the number is zero or not
# then it will validate the number
# finally it returns true or false
def solve(board):
    zero = is_empty(board)
    if not zero:
        return True
    else:
        row, col = zero
    
    for i in range(1, 10):
        if is_valid(i, row, col, board):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False
    
# this function simply checks if the number is a 0 or not
def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

# this is the worker function. It checks all the horizonzal and vertical lines
# to make sure all the number are unique
# then it checks the 3 by 3 box to make sure they are also unique
def is_valid(marker, row, col, board):
    for i in range(N):
        if board[row][i] == marker and i != col:
            return False
    for j in range(N):
        if board[j][col] == marker and j != row:
            return False

    # three by three boxes
    t_by_t_one = (row//3) * 3
    t_by_t_two = (col//3) * 3

    # if any of the numbers match it will return false
    for i in range(3):
        for j in range(3):
            r = t_by_t_one + i
            c = t_by_t_two + j
            if board[r][c] == marker:
                return False

    return True

# prints our the current board
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()

# this function is what the main will call when it needs to solve the board
def input(board, x):

    printing(board)

    # if it words it will return a boolean 0 or 1 to trigger the success message
    if(solve(board)):
        print("-----------------")
        printing(board)
        print("Solved")
        return board, 0
    else:
        print("-----------------")
        print("No Solution")
        return board, 1


