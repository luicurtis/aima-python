# Question 4 (Approximate)

import csp
from a2_q1 import rand_graph
from a2_q2 import check_teams
import time
from csp import CSP, UniversalDict, different_values_constraint

class CSP_modified(CSP):
    def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem. If variables is empty, it becomes domains.keys()."""
        super().__init__(variables, domains, neighbors, constraints)
        self.nuassigns = 0

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        self.nuassigns += 1      # added to count when var is unassigned
        if var in assignment:
            del assignment[var]

def MapColoringCSP_modified(colors, neighbors):
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    # edited return value to use CSP_modified
    return CSP_modified(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)

def run_q4():
    n = 105  # Number of people
    graphs = [rand_graph(0.1, 31), rand_graph(0.2, 31), rand_graph(0.3, 31),
            rand_graph(0.4, 31), rand_graph(0.5, 31), rand_graph(0.6, 31)]
    for i in range(len(graphs)):
        neighbor = graphs[i]
        
        if (i == 0): 
            print("*** Testing: rand_graph(0.1, 105) ***")
        elif (i == 1):
            print("*** Testing: rand_graph(0.2, 105) ***")
        elif (i == 2):
            print("*** Testing: rand_graph(0.3, 105) ***")
        elif (i == 3):
            print("*** Testing: rand_graph(0.4, 105) ***")
        elif (i == 4):
            print("*** Testing: rand_graph(0.5, 105) ***")
        elif (i == 5):
            print("*** Testing: rand_graph(0.6, 105) ***")
        
        result = None
        i = 0   # team size counter
        variables = list(range(i))
        cspProblem = MapColoringCSP_modified(variables, neighbor)
        totAssigned = 0
        totUnassigned = 0
        start_time = time.time()
        # Starting with one team, try backtracking. If it fails, increase number of teams by 1
        # and try again
        while not result:
            i += 1
            variables = list(range(i))
            cspProblem = MapColoringCSP_modified(variables, neighbor)
            result = csp.min_conflicts(cspProblem, 10000) # steps of 10000 to reduce running time and complexity
            totAssigned += cspProblem.nassigns
            totUnassigned += cspProblem.nuassigns

        elapsed_time = time.time() - start_time

        numTeams = len(set(result.values()))
        totalNumConst = 0
        # Count the total number of constraints in the graph
        for i in neighbor:
            totalNumConst += len(neighbor[i])
        totalNumConst = int(totalNumConst / 2)  # divide by 2 to avoid double counting
                                                # i.e) Xi != Xj, Xj != Xi is the same
                    
        print("FRIENDSHIP GRAPH: \n", neighbor)
        print("RESULT: ", result)
        print("SOLVEABLE: ", check_teams(neighbor, result))
        print("MIN NUM TEAMS: ", numTeams)
        print("RUNNING TIME: ", elapsed_time)
        print("NUM ASSIGNMENTS: ", totAssigned)
        print("NUM UNASSIGNMENTS: ", totUnassigned)
        print("NUM TOTAL CONSTRAINTS: ", totalNumConst)
        print()
    return None

def main():
    print()
    run_q4()

if __name__ == '__main__':
    main()
