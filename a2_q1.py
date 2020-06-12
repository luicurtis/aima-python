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
    x = 0
    for i in range(n):
        for j in range(x, n):
            if i != j:
                connect = random.random() < p
                if connect and j not in graph[i]:
                    graph[i].append(j)
                    graph[j].append(i)
        x += 1
    
    for i in range(n):
        graph[i].sort()
    return graph
    
def main():
    # TESTING rand_graph(p, n)
    print(rand_graph(0.1, 8))

if __name__ == '__main__':
    main()


