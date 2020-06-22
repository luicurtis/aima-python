# a3.py
import random

def printBoard(board):
    ''' Print the game board. Input board is a list '''
    i = 0
    while i < 9:
        print("    ", board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("    ---+---+---")
        i += 3

def firstMove():
    ''' Determine who goes first '''
    turn = random.choice([0, 1])
    if (turn):
        print("The player will go first. \nThe player will use X and the computer will use O")
        return 'player'
    else:
        print("The computer will go first. \nThe computer will use X and the player will use O")
        return 'computer'

def checkWin(board, symbol):
    ''' Check if the current board is a win for the current turn'''
    i = 0
    # horizontal lines
    while i < 9:
        if (board[i] == symbol and board[i+1] == symbol and board[i+2] == symbol):
            return True
        i += 3
    
    # vertical lines
    i = 0
    while i < 3:
        if (board[i] == symbol and board[i+3] == symbol and board[i+6] == symbol):
            return True
        i += 1
    
    # diagonal lines
    if ((board[0] == symbol and board[4] == symbol and board[8] == symbol) or \
         board[2] == symbol and board[4] == symbol and board[6] == symbol):
         return True

def playerMove(board, symbol):
    legalMoves = []
    tempBoard = [' '] * 9

    for i in range(9):
        # find empty positions
        # source: https://stackoverflow.com/questions/8411889/how-do-i-check-in-python-if-an-element-of-a-list-is-empty
        if board[i] == ' ':
            legalMoves.append(str(i+1))
            tempBoard[i] = str(i+1)
        else:
            tempBoard[i] = board[i]

    legalMoves.sort()
    
    move = ''

    while move not in legalMoves:
        print("The following are your possible legal moves:", str(legalMoves)[1:-1])
        printBoard(tempBoard)
        move = input()

    board[int(move)-1] = symbol     # make the move


def play_a_new_game():
    # intialize a new board
    # source: https://stackoverflow.com/questions/521674/initializing-a-list-to-a-known-number-of-elements-in-python
    board = [' '] * 9

    # Determine who goes first
    turn = firstMove()
    playerSymbol = 'X' if turn == "player" else 'O'
    computerSymbol = 'O' if turn == "player" else 'X'
    

    # Testing

    board[0] = 'X'
    playerMove(board, 'X')
    playerMove(board, 'X')
    print(checkWin(board, 'X'))
    printBoard(board)
    return

if __name__ == '__main__':    
    play_a_new_game()