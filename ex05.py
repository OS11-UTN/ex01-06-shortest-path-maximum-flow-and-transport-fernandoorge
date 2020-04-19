##############################################################################
#   OS11 LOGISTICS
#   Author: Orge, Fernando Gabriel
#   EX5
#       Basic Example of Maximum Flow with Ford-Fulkerson Algorithm
#
#   Solution:
#       NN = np.array( [[0, 1, 1, 0, 0, 0],
#                       [0, 0, 0, 1, 0, 1],
#                       [0, 0, 0, 0, 1, 0],
#                       [0, 0, 0, 0, 0, 1],
#                       [0, 0, 0, 0, 0, 1],
#                       [0, 0, 0, 0, 0, 0]])
#
##############################################################################
import numpy        as      np
import logistics    as      lg
from scipy.optimize import  linprog
from itertools      import  permutations

nodes = ['s','2','3','4','5','t']
G     = np.array([[0, 7, 1, 0, 0, 0],
                  [0, 0, 0, 2, 0, 3],
                  [0, 0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0, 0]])

###############################################################################
###############################################################################
# This piece of code is used to test the DFS algorithm with a Node-Node Matrix
# We took all nodes permutations and execute DFS for each pair of nodes
# Then we print all paths
perm = permutations(range(6), 2)
for pair in perm:
    print('Search a path between %s using DFS algorithm' 
        % lg.convert_path(pair, nodes))
    path = lg.dfs(G,pair[0],pair[1])
    print('    The path found was = %s\n' % lg.convert_path(path, nodes))

###############################################################################
###############################################################################
max_flow, fbG = lg.ford_fulk(G, 0, 5)
print('Maximum flow solution = %d' % max_flow)
print('Feedback Graph = \n%s\n' % fbG)

###############################################################################
###############################################################################
# Use graph from Exercise02
G = np.array([[0, 2, 1, 0, 0, 0],
              [0, 0, 0, 2, 0, 5],
              [0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 2],
              [0, 0, 0, 0, 0, 0]])
max_flow, fbG = lg.ford_fulk(G, 0, 5)
print('The expected max flow = 3')
print('Maximum flow solution = %d' % max_flow)
print('Feedback Graph = \n%s\n' % fbG)

###############################################################################
###############################################################################
# Use graph from Exercise03
G = np.array([[0, 2, 2, 0, 0, 0],
              [0, 0, 0, 2, 0, 5],
              [0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 2],
              [0, 0, 0, 0, 0, 0]])
max_flow, fbG = lg.ford_fulk(G, 0, 5)
print('The expected max flow = 4')
print('Maximum flow solution = %d' % max_flow)
print('Feedback Graph = \n%s\n' % fbG)
