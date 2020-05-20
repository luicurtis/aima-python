# a1.py

from search import *
import random
import time

# ...
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

def astar_search_modified(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    
    h = memoize(h or problem.h, 'h')

    start_time = time.time()
    
    result, numRemoved = best_first_graph_search_modified(problem, lambda n: n.path_cost + h(n), display)

    
    print(numRemoved)
    

    elapsed_time = time.time() - start_time 
    print("\nMisplaced Tile Total Running Time:", f'{elapsed_time}s')
    

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

def main():
    initialState = make_rand_8puzzle()
    display(initialState)
    puzzle = EightPuzzle(initialState)

    astar_search_modified(puzzle)


if __name__ == '__main__':
    main()