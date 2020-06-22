# a3.py

def printBoard(board):
    i = 0;
    while i < 9:
        print("", board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("----------")
        i += 3


def play_a_new_game():
    return

if __name__ == '__main__':
    board = list(range(0, 9))
    printBoard(board)