# Question 2 (warm-up: Checking Solutions)

# Description:  Returns a new random graph with n nodes numbered 0 to n−1 such that
#               every different pair of nodes is connected with probability p.
#               Assume n>1, and 0≤p≤1.
#
# Input:    graph - input graph
#           csp_sol - CSP solution dictionary
def check_teams(graph, csp_sol):
    solvable = True
    # create teams from csp_sol
    # Sources:
    # - https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-a-list
    numTeams = len(set(csp_sol.values()))
    teams = {teamNum: [] for teamNum in set(csp_sol.values())} 
    for i in csp_sol:
        teams[csp_sol[i]].append(i)

    # cross reference the graph relationship to ensure no matches
    for i in graph:
        currKeyTeam = csp_sol[i]
        # print("Key: ", i)
        # print("Team: ", currKeyTeam)
        for j in range(len(graph[i])):
            # print("Checking Relationships with: ", graph[i][j])
            if graph[i][j] in teams[currKeyTeam]:
                solvable = False
                return solvable

    return solvable


# TESTING check_teams(graph, csp_sol)
# graph = {0: [1, 2], 1: [0], 2: [0], 3: []}
# csp_sol = {0:0, 1:1, 2:1, 3:0}
# print(check_teams(graph, csp_sol))