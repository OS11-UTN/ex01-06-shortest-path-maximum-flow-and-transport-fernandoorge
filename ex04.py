##############################################################################
#   OS11 LOGISTICS
#   Author: Orge, Fernando Gabriel
#   EX04
#       Basic Example of Maximum Flow Problem
#
#   Formulation
#       This is a special case of the minimum cost flow problem, that can be 
#       modeled as
#               minimize    c*x
#               subject to 
#                           NA*x = b
#                           l <= x <= u
#               c  is the costs vector
#               X  is the decision variables vector
#               NA is the node-arc matrix
#               b  is the associated demand/supply for each node
#               l  is the lower capacity bound
#               u  is the upper capacity bound
#      
#   Solution
#       For this problem
#           b(i) = 0, for all node i in N
#           Cij  = 0, for all arc (i,j) in A
#           Lij  = 0, for all arc (i,j) in A (no lower bound)
#           Uij  = k, for all arc (i,j) in A (k-integer upped bound)
#       List of arcs
#           (S,2) => Uij = 7
#           (S,3) => Uij = 1
#           (2,4) => Uij = 2
#           (2,T) => Uij = 3
#           (3,5) => Uij = 2
#           (4,T) => Uij = 1
#           (5,T) => Uij = 1
#       We have to add an additional arc (t,s) with Cts = -1 and Uts = +inf
#       Hence, the Node-Node Matrix will be
#             S 2 3 4 5 T
#           S 0 1 1 0 0 0
#           2 0 0 0 1 0 1
#           3 0 0 0 0 1 0
#           4 0 0 0 0 0 1
#           5 0 0 0 0 0 1
#           T 1 0 0 0 0 0
#       the upper bound vector (length = |A| = m)
#           u = [7, 1, 2, 3, 2, 1, 2, +inf]
#       the lower bound vector (length = |A| = m)
#           l = [0, 0, 0, 0, 0, 0, 0, 0]
#       the b vector (length = |N| = n)
#           b = [0, 0, 0, 0, 0, 0]
#       and the costs vector will be (length = |A| = m)
#           c = [0, 0, 0, 0, 0, 0, 0, -1]
#
#       Result: The maximum flow across the network is 5 (five)
##############################################################################
import numpy     as np
import logistics as lg
from   scipy.optimize import  linprog

nodes = ['s','2','3','4','5','t']


NN = np.array([[0, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0]])
               
NA, arcs = lg.nn2na(NN) 
c = np.array([0, 0, 0, 0, 0, 0, 0,  -1])
u = np.array([7, 1, 2, 3, 2, 1, 2, 100])
l = np.array([0, 0, 0, 0, 0, 0, 0,   0])
b = np.array([0, 0, 0, 0, 0, 0])

##############################################################################
# Inputs lo linprog algorithm
C   = c
Aeq = NA
beq = b
bounds = []
for k in range(0, len(l)):
    bound_tuple = (l[k], u[k])
    bounds.append(bound_tuple)

print('\t OPTIMIZER INPUTS                         \n'
      '\t     Cost vector                   :   %s \n'
      '\t     A_eq Node-Arc matrix          : \n%s \n'
      '\t     b_eq demand-supply vector     :   %s \n'
      '\t     Bounds of each X arc variable :   %s \n' % (C, Aeq, beq, bounds))

name_method = 'simplex'
print('\n*****************************************************************')
print('\t SOLVING PROBLEM WITH: %s' % name_method)
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method=name_method)
print('\t Solution to the problem:')
print('\t   The raw solution will be: %s' % res.x)
for k in range(0, len(res.x)):
    if res.x[k] > 0:
        print('\t\t %d units must be moved across %s arc.' 
            % (res.x[k], str(lg.convert_arc(arcs[k], nodes))))
print('\t   The maximum flow will be: %0.2f ' % abs(res.fun))
print('*****************************************************************\n')
