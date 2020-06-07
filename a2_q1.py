# Question 1 (warm-up: Erdos-Renyi random graphs)

import random

# Description:  Returns a new random graph with n nodes numbered 0 to n−1 such that
#               every different pair of nodes is connected with probability p.
#               Assume n>1, and 0≤p≤1.
#
# Input:    p - probability
#           n - number of nodes
def rand_graph(p, n):
    # Sources Used:
    #   - https://stackoverflow.com/questions/5886987/true-or-false-output-based-on-a-probability
    #   - https://www.geeksforgeeks.org/python-initializing-dictionary-with-empty-lists/

    graph = {person: [] for person in range(n)} 
    for i in range(n):
        for j in range(n):
            if i != j:
                connect = random.random() < p
                if connect:
                    graph[i].append(j)
    
    print(len(graph))
    print((graph[0][0]))
    return graph
    
# TESTING rand_graph(p, n)
print(rand_graph(0.5, 8))

