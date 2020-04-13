##############################################################################
#   OS11 LOGISTICS
#   Author: Orge, Fernando Gabriel
#   EX3
#       Basic Example of Shortest Path Problem
#       with Dijkstra algorithm
#
#   Solution:
#       Graph in EX01
#           Shortest path solution: ['s', '2', '4', 't']
#           Cumulative distance   : [0.0, 2.0, 4.0, 5.0]
#           Minimum distance      : 5
#       
#       Graph in EX02
#           Shortest path solution: ['s', '3', '5', 't']
#           Cumulative distance   : [0.0, 1.0, 3.0, 5.0]
#           Minimum distance      : 5
##############################################################################
import numpy     as np
import logistics as lg

nodes = ['s','2','3','4','5','t']

# NN matrix for graph in ex01
NN    = np.array([[0, 2, 2, 0, 0, 0],
                  [0, 0, 0, 2, 0, 5],
                  [0, 0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0, 0]])
lg.dijkstra_alg(NN, nodes)

# NN matrix for graph in ex02
NN    = np.array([[0, 2, 1, 0, 0, 0],
                  [0, 0, 0, 2, 0, 5],
                  [0, 0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0, 0]])
lg.dijkstra_alg(NN, nodes)
