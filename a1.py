# a1.py

from search import *
import random
import time

class DuckPuzzle(Problem):
    """ Adapted from EightPuzzle(Problem) in aima-python library. 
    sliding tiles numbered from 1 to 8 on a board that is shaped like a duck
    +--+--+
    |  |  |
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
        |  |  |  |
        +--+--+--+
    1 2
    3 4 5 6   goal state
      7 8 *    """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem. """
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square == 0:
            possible_actions.remove('LEFT')
            possible_actions.remove('UP')
        elif index_blank_square == 1:
            possible_actions.remove('UP')
            possible_actions.remove('RIGHT')
        elif index_blank_square == 2:
            possible_actions.remove('LEFT')
            possible_actions.remove('DOWN')
        elif index_blank_square == 3:
            None
        elif index_blank_square == 4:
            possible_actions.remove('UP')
        elif index_blank_square == 5:
            possible_actions.remove('UP')
            possible_actions.remove('RIGHT')
        elif index_blank_square == 6:
            possible_actions.remove('LEFT')
            possible_actions.remove('DOWN')
        elif index_blank_square == 7:
            possible_actions.remove('DOWN')
        elif index_blank_square == 8:
            possible_actions.remove('DOWN')
            possible_actions.remove('RIGHT')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))
        
def make_rand_8puzzle():
    # Generate random list of numbers from 0 to 8
    # Help from: https://stackoverflow.com/questions/9755538/how-do-i-create-a-list-of-random-numbers-without-duplicates
    initialState = tuple(random.sample(range(9), 9))  
    puzzle = EightPuzzle(initialState)
    # Ensure puzzle is solvable
    while not puzzle.check_solvability(initialState):
        initialState = tuple(random.sample(range(9), 9))
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
    return None

def astar_search_modified(problem, method, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""

    if (method == "misplaced" or method == "manhattan"):
        h = memoize(h or problem.h, 'h')
    else:
        initNode = Node(problem.initial)
        if (problem.h(initNode) > manhattan_distance_h(initNode)):
            h = memoize(h, 'h')
        else:
            h = memoize(manhattan_distance_h, 'h')
 
    start_time = time.time()
    result, numRemoved = best_first_graph_search_modified(problem, lambda n: n.path_cost + h(n), display)
    elapsed_time = time.time() - start_time 

    if method == "misplaced":
        print("\nMisplaced Tile Heuristic:")
    elif method == "manhattan":
        print("\nManhattan Distance Heuristic:")
    else:
        print("\nMax of Misplaced Tile and Manhattan Distance Heuristic:")
    
    
    print("Total Running Time:", f'{elapsed_time}')
    print("Length of Solution: ", len(result.path()))
    print("Total Number of Nodes removed from frontier: ", numRemoved)
    

def best_first_graph_search_modified(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    numRemoved = 0  # added pop counter
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        numRemoved += 1
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node, numRemoved     # added numRemoved
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None

def manhattan_distance_h(node):
    # create 9 by 9 Manhattan reference table
    # indexed by [tile name][location]
    table = [[4, 3, 2, 3, 2, 1, 2, 1, 0],   \
             [0, 1, 2, 1, 2, 3, 2, 3, 4],   \
             [1, 0, 1, 2, 1, 2, 3, 2, 3],   \
             [2, 1, 0, 3, 2, 1, 4, 3, 2],   \
             [1, 2, 3, 0, 1, 2, 1, 2, 3],   \
             [2, 1, 2, 1, 0, 1, 2, 1, 2],   \
             [3, 2, 1, 2, 1, 0, 3, 2, 1],   \
             [2, 3, 4, 1, 2, 3, 0, 1, 2],   \
             [3, 2, 3, 2, 1 ,2, 1, 0, 1]]

    distance = 0;
    for i in range(0, 9):
        tile = node.state[i]
        if (tile != 0):
            #Dont want to count the blank space
            distance += table[tile][i]
    #print("Manhattan Distance: ", distance)
    return distance

def displayDuck(state):
    for i in range(0, 2):
        if state[i] == 0:
            print("*", end = ' '),
        else:
            print(state[i], end = ' '),
    print(),
    for i in range(2, 6):
        if i == 2:
            if state[i] == 0:
                print("*", end = ' '),
            else:
                print(state[i], end = ' '),
        else:
            if state[i] == 0:
                print("*", end = ' '),
            else:
                print(state[i], end = ' ')

    for i in range(6, 9):
        if i == 6:
            if state[i] == 0:
                print("\n *", end = ' '),
            else:
                print("\n ", state[i], end = ' '),
        else:
            if state[i] == 0:
                print("*", end = ' '),
            else:
                print(state[i], end = ' '),
    print()

    #print(" ", state[6], state[7], state[8]),

    return None



def main():
    # make random 10 puzzles and solve them with differnt techniques
    # for i in range(0,10):
    initialState = make_rand_8puzzle()
        
        #display(initialState)
    #     puzzle = EightPuzzle(initialState)
    #     print(initialState)
    #     astar_search_modified(puzzle, "misplaced")
    #     astar_search_modified(puzzle, "manhattan", manhattan_distance_h)
    #     astar_search_modified(puzzle, "max")
    displayDuck(initialState)

if __name__ == '__main__':
    main()