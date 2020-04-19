##############################################################################
#   OS11 LOGISTICS
#   Author: Orge, Fernando Gabriel
#   EX1
#       Basic Example of Shortest Path Problem
#
#   Solution:
#       The graph can be model as a Node-Node matrix as follows
#       NN = np.array( [[0, 1, 1, 0, 0, 0],
#                       [0, 0, 0, 1, 0, 1],
#                       [0, 0, 0, 0, 1, 0],
#                       [0, 0, 0, 0, 0, 1],
#                       [0, 0, 0, 0, 0, 1],
#                       [0, 0, 0, 0, 0, 0]])
#
#       To find the shortest path we model the problem as
#           minimum cost flow problem
#       hence, the solution can be found by
#           min {C*X^t}
#               subject to 
#               AX = b
#       with
#           C = [2,2,2,5,2,1,2] 	the cost of each arc
#           X = [x1,x2,...,xn]  	binary decision of taking xi path
#           b = [1,0,0,0,0,0,-1]	an imaginary load will be moved 
#                                   from node s to node t
#           A = is the node-arc matrix obtained from the node-node one
#
#   Results:
#       The raw solution will be: [1. 0. 1. 0. 0. 1. 0.]
#           Arc ('s', '2') must be taken.
#           Arc ('2', '4') must be taken.
#           Arc ('4', 't') must be taken.
#       The minimum cost will be: 5.00 
##############################################################################
import numpy     	as 		np
import logistics    as      lg
from scipy.optimize import 	linprog

nodes     = ['s','2','3','4','5','t']
NN        = np.array([[0, 1, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 1],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0]])
C         = np.array([2, 2, 2, 5, 2, 1, 2])
Aeq, arcs = lg.nn2na(NN)
beq       = np.array([1, 0, 0, 0, 0, -1])
bounds    = tuple([(0, None) for arcs in range(0, Aeq.shape[1])])

print('## Optimizer inputs ## \n'
      'Cost vector                   :   %s \n'
      'A_eq Node-Arc matrix          : \n%s \n'
      'b_eq demand-supply vector     :   %s \n'
      'Bounds of each X arc variable :   %s \n' % (C, Aeq, beq, bounds))

# OPTIMIZE:
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method='simplex')
print(res)

# GET THE SOLUTION:
print('## Results ##')
print('The raw solution will be: %s' % res.x)
for k in range(0, len(res.x)):
    if res.x[k] == 1:
        print('    Arc %s must be taken.' % str(lg.convert_arc(arcs[k], nodes)))
print('The minimum cost will be: %0.2f. ' % res.fun)
