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

def main():
    # Testing check_teams(graph, csp_sol)
    graph = {0: [1, 2], 1: [0], 2: [0], 3: []}
    csp_sol = {0:0, 1:1, 2:1, 3:0}
    print(check_teams(graph, csp_sol))

    # If no one is friends with anyone else, then only 1 team
    # the entire group of n people — is needed.
    graph = {0: [], 1: [], 2: [], 3: []}
    csp_sol = {0:0, 1:0, 2:0, 3:0}
    print(check_teams(graph, csp_sol))

    # If everyone is friends with everyone else, then n teams are needed.
    # Everyone would have to be on a team by themselves.
    graph = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}
    csp_sol = {0:0, 1:1, 2:2, 3:3}
    print(check_teams(graph, csp_sol))

    # If there is someone who is friends with everyone else, 
    # then they must be on a team by themselves
    graph = {0: [1, 2, 3], 1: [], 2: [], 3: []}
    csp_sol = {0:0, 1:1, 2:1, 3:1}
    print(check_teams(graph, csp_sol))

    # Someone who is friends with no one can be added to any team.
    graph = {0: [1, 2, 3], 1: [], 2: [], 3: []}
    csp_sol = {0:0, 1:1, 2:1, 3:1}
    print(check_teams(graph, csp_sol))
if __name__ == '__main__':
    main()
