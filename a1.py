# a1.py

from search import *
import random

# ...
def make_rand_8puzzle():
    # Generate random list of numbers from 0 to 8
    # Help from: https://stackoverflow.com/questions/9755538/how-do-i-create-a-list-of-random-numbers-without-duplicates
    initialState = random.sample(range(9), 9)
  
    puzzle = EightPuzzle(initialState)

    while not puzzle.check_solvability(initialState):
        initialState = random.sample(range(9), 9)

    return initialState

def display(state):
    i = 0
    j = 0
    while i < 9:
        if state[i] == 0:
            if j != 2:
                print("*", end = ' ')
            else:
                print("*")
        else:
            if j != 2:
                print(state[i], end = ' ')
            else:
                print(state[i])

        if j == 2:
            j = -1
        j += 1
        i += 1
    return



def main():
    display(make_rand_8puzzle())



if __name__ == '__main__':
    main()