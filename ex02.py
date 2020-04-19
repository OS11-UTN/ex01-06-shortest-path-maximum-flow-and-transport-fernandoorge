##############################################################################
#   OS11 LOGISTICS
#   Author: Orge, Fernando Gabriel
#   EX2
#       Basic Example of Shortest Path Problem
#       with different algorithms
#
#   Solution:
#       This new graph has the same NN matrix as the previous one, hence,
#       it can be model as follows
#       NN = np.array( [[0, 1, 1, 0, 0, 0],
#                       [0, 0, 0, 1, 0, 1],
#                       [0, 0, 0, 0, 1, 0],
#                       [0, 0, 0, 0, 0, 1],
#                       [0, 0, 0, 0, 0, 1],
#                       [0, 0, 0, 0, 0, 0]])
#
#       However the Cost Vector is now equal to
#           C = [2,1,2,5,2,1,2] 	the cost of each arc
#
#       The X vector (decision vars) is the same
#           X = [x1,x2,...,xn]  	binary decision of taking xi path
#
#       and the RHS of the equation is also the same
#           b = [1,0,0,0,0,0,-1]	an imaginary load will be moved 
#                                   from node s to node t
#           A = is the node-arc matrix obtained from the node-node one
#
#       Relevant notes:
#           
#           SOLVING PROBLEM WITH: interior-point
#               the interior-point method is not able to find a solution.
#
#           SOLVING PROBLEM WITH: simplex
#               the simplex algorithm gives us the optimal solution.
#	            The raw solution will be: [0. 1. 0. 0. 1. 0. 1.]
#                   Arc ('s', '3') must be taken.
#                   Arc ('3', '5') must be taken.
#                   Arc ('5', 't') must be taken.
#               The minimum cost will be: 5.00. 
#
##############################################################################
import numpy        as      np
import logistics    as      lg
from scipy.optimize import  linprog

nodes           = ['s','2','3','4','5','t']
NN              = np.array([[0, 1, 1, 0, 0, 0],
                            [0, 0, 0, 1, 0, 1],
                            [0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0]])
C               = np.array([2, 1, 2, 5, 2, 1, 2])
Aeq, arcs       = lg.nn2na(NN)
beq             = np.array([1, 0, 0, 0, 0, -1])
bounds          = tuple([(0, None) for arcs in range(0, Aeq.shape[1])])

print('## Optimizer inputs ## \n'
      'Cost vector                   :   %s \n'
      'A_eq Node-Arc matrix          : \n%s \n'
      'b_eq demand-supply vector     :   %s \n'
      'Bounds of each X arc variable :   %s \n' % (C, Aeq, beq, bounds))

for name_method in 'interior-point', 'simplex':
    print('\n*****************************************************************')
    print('\t SOLVING PROBLEM WITH: %s' % name_method)
    res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method=name_method)
    print('\t Solution to the problem:')
    print('\t   The raw solution will be: %s' % res.x)
    for k in range(0, len(res.x)):
        if res.x[k] == 1:
            print('\t\t Arc %s must be taken.' % str(lg.convert_arc(arcs[k], nodes)))
    print('\t   The minimum cost will be: %0.2f ' % res.fun)
    print('*****************************************************************\n')
