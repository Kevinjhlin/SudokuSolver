# random sudoku board i found on google
board1 = [
    [0, 7, 0, 0, 0, 0, 0, 0, 9],
    [5, 1, 0, 4, 2, 0, 6, 0, 0],
    [0, 8, 0, 3, 0, 0, 7, 0, 0],
    [0, 0, 8, 0, 0, 1, 3, 7, 0],
    [0, 2, 3, 0, 8, 0, 0, 4, 0],
    [4, 0, 0, 9, 0, 0, 1, 0, 0],
    [9, 6, 2, 8, 0, 0, 0, 3, 0],
    [7, 0, 0, 2, 0, 3, 0, 9, 6]
]


def print_board(board):
    '''
    print a full board
    :param board: list [][]
    :return: board in print format
    '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    '''
    find the next empty space on board.
    :param board: list [][]
    :return: doublet
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j


def is_valid(board, position, input):
    # validate row and column for same number
    for i in range(0, len(board)):
        if board[position[0]][i] == input or board[i][position[1]] == input:
            return False

    # validate if square contains input number
    square_y = position[0] // 3
    square_x = position[1] // 3

    for i in range(square_x, square_x + 3):
        for j in range(square_y, square_y + 3):
            if board[i][j] == input and (i, j) != position:
                return False

    return True


def solve(board):
    '''
    Core code to solve for the sudoku.
    :param board: list [][]
    :return: completed board
    '''
    empty = find_empty(board)

    if empty:
        row, col = empty
    else:
        return True

    for i in range(1, 10):
        if is_valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


if __name__ == '__main__':
    print_board(board1)
    solve(board1)
    print("And the solveed version is this:")
    print_board(board1)
