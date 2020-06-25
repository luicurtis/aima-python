# a3.py
''' 

'''
import random

def printBoard(board):
    ''' Print the game board. Input board is a list '''
    i = 0
    while i < 9:
        print("    ", board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("    ---+---+---")
        i += 3
    return None

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
    ''' Check if the current board is a win for the current turn
    
        Returns true if it is a winning board, else false'''
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

    return False

def playerMove(board, symbol):
    ''' Allow the player to enter their move '''
    legalMoves = []
    tempBoard = [' '] * 9

    for i in range(len(board)):
        # find empty positions and create a temp board to print to user
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
        print("Please input one of the following followed by <enter>:", str(legalMoves)[1:-1])
        move = input()

    board[int(move)-1] = symbol     # make the move
    return None

def legalMoves(board):
    ''' return a list of all legal moves for the board position '''
    legalMoves = []
    for i in range(len(board)):
        if board[i] == ' ':
            legalMoves.append(str(i))
    legalMoves.sort()
    return legalMoves

def makeRandmove(board, moves, symbol):
    move = int(random.choice(moves))
    board[move] = symbol
    return None

def randPlayout(board, compSymbol, playSymbol, move):
    ''' A random playout is when the computer simulates playing the game until it is over.
        During a random playout, the computer makes random moves for each player until 
        a win, loss, or draw is reached 
        
        Returns true if the computer won, else false'''

    # copy the board to avoid changing the original
    tempBoard = [' '] * 9
    for i in range(len(board)):
        tempBoard[i] = board[i]
    
    tempBoard[move] = compSymbol    # make the given move
    turn = playSymbol               # set the local turn to the player
    
    while not checkWin(tempBoard, turn):
        legalMoves = legalMoves(tempBoard)
        makeRandmove(tempBoard, legalMoves, turn)

    
    # return true if computer won, else false
    return None


def play_a_new_game():
    # intialize a new board
    board = [' '] * 9       # ' ' represents a free space
    numRandPlayouts = 50    # 

    # Determine who goes first
    turn = firstMove()
    playerSymbol = 'X' if turn == "player" else 'O'
    computerSymbol = 'O' if turn == "player" else 'X'
    

    # Testing
    possibleMoves = legalMoves(board)
    # numWins = [0] * len(possibleMoves)
    # print(possibleMoves)
    # print(numWins)
    # for i in range(len(possibleMoves)):
    #     for j in numRandPlayouts:
    #         # Do numRandPlayouts of times 
    #         # if rand playout is a win, then increment that move
    #         if randPlayout(board, computerSymbol, playerSymbol, possibleMoves[i]):
    #             numWins[j] += 1

    makeRandmove(board, possibleMoves, 'X')
    printBoard(board)



    return None

if __name__ == '__main__':    
    play_a_new_game()