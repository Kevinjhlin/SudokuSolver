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

if __name__ == '__main__':
    print_board(board1)