# Question 3 (Exact)

import csp
from a2_q1 import rand_graph
from a2_q2 import check_teams

# Adapted from https://www2.cs.sfu.ca/CourseCentral/310/tjd/chp6_csp.html
# If X=a and Y=b satisfies the constraints on X and Y, then True is returned.
# Otherwise,. False is returned.

def constraints(X, a, Y, b):
  try:
    return cnstr[(X,Y)](a,b)
  except KeyError:  # if a pair is not in the table, then there are no constraints
    return True     # on X an Y, and so X=a and Y=b is acceptable


n = 31  # Global variable for n

neighbor = rand_graph(0.1, n)   # rand_graph returns a dict of {var:[var,...]} that for each variable
                                # lists the other variables that participate in constraints
print(neighbor)

variables = list(neighbor.keys())  # variables are the keys

# Initialize domain for each varaible as a list from 0 to 30
# i.e)  The maximum way to divide teams is to have 30 individual teams.
#       Each person can be in any team in this case
domain = {person: list(range(n)) for person in range(n)}


cnstr = {}
for i in neighbor:
    # Create constraint (!=) relationship with person, i, and all of its friends, j.
    for j in range(len(neighbor[i])):
        cnstr[(i,neighbor[i][j])] = lambda x,y: x != y

