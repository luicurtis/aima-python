# Question 3 (Exact)

import csp
from a2_q1 import rand_graph
from a2_q2 import check_teams
import time
from csp import CSP, mrv, lcv, forward_checking, mac, UniversalDict, different_values_constraint

# Subclass of CSP from csp.py
# - Created subclass inorder to add functionality when unassigned is called
#   to increment the number of unassigns (nuassigns) variable


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
    """Make a CSP for the problem of coloring a map with different colors
    for any two adjacent regions. Arguments are a list of colors, and a
    dict of {region: [neighbor,...]} entries. This dict may also be
    specified as a string of the form defined by parse_neighbors."""
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    # edited return value to use CSP_modified
    return CSP_modified(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)


def run_q3():

    return


n = 31  # Number of people
graphs = [rand_graph(0.1, 31), rand_graph(0.2, 31), rand_graph(0.3, 31),
          rand_graph(0.4, 31), rand_graph(0.5, 31), rand_graph(0.6, 31)]

neighbor = rand_graph(0.1, n)  # rand_graph returns a dict of {var:[var,...]} that for each variable
								# lists the other variables that participate in constraints
print(neighbor)

result = None
i = 0   # team size counter
start_time = time.time()
while not result:
    i += 1
    variables = list(range(i))
    cspProblem = MapColoringCSP_modified(variables, neighbor)
    result = csp.backtracking_search(cspProblem, select_unassigned_variable=mrv, \
                                order_domain_values=lcv, inference=forward_checking)
elapsed_time = time.time() - start_time

numTeams = len(set(result.values()))

print()
print("RESULT: ", result)
print("RUNNING TIME: ", elapsed_time)
print("SOLVEABLE: ", check_teams(neighbor, result))
print("MIN NUM TEAMS: ", numTeams)
print("NUM ASSIGNMENTS: ", cspProblem.nassigns)
print("NUM UNASSIGNMENTS: ", cspProblem.nuassigns)
# print("NUM CONFLICTS: ", numConflicts)


# def main():


# if __name__ == '__main__':
#     main()
