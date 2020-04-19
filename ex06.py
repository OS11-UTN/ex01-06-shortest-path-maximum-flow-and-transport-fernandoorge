##############################################################################
#   OS11 LOGISTICS
#   Author: Orge, Fernando Gabriel
#   EX06
#       Transport model example
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
#           N = N1 U N2 where N1 is the set of supplies nodes {1, 2, 3}
#                             N2 is the set of demands  nodes {a, b}
#
#           for all (i,j) in A : i in N1 and j in N2
#
#       the Node-Node Matrix will be
#             1 2 3 a b  
#           1 0 0 0 1 1  
#           2 0 0 0 1 1  
#           3 0 0 0 1 1  
#           a 0 0 0 0 0  
#           b 0 0 0 0 0  
#
#       List of arcs
#           (1,a) => Cij = 10
#           (1,b) => Cij = 20
#           (2,a) => Cij = 10
#           (2,b) => Cij = 10
#           (3,a) => Cij = 10
#           (3,b) => Cij = 30
#
#       the costs vector                    
#           c = [10, 20, 10, 10, 10, 30]                (length = |A| = m)
#       the upper bound vector              
#           u = [+inf, +inf, +inf, +inf, +inf, +inf]    (length = |A| = m)
#       the lower bound vector              
#           l = [0, 0, 0, 0, 0, 0]                      (length = |A| = m)
#       the b vector                        
#           b = [10, 20, 15, -25, -20]                  (length = |N| = n)
#
#   Results
#       SOLVING PROBLEM WITH SIMPLEX
#	        The raw solution will be: [10.  0.  0. 20. 15.  0.]
#	            10 units will be moved across 1a arc
#	             0 units will be moved across 1b arc
#	             0 units will be moved across 2a arc
#	            20 units will be moved across 2b arc
#	            15 units will be moved across 3a arc
#	             0 units will be moved across 3b arc
#	        The minimum cost will be: 450.00
##############################################################################
import numpy     as np
import logistics as lg
from   scipy.optimize import  linprog

nodes = ['1','2','3','a','b']


NN = np.array([[0, 0, 0, 1, 1],
               [0, 0, 0, 1, 1],
               [0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]])
               
NA, arcs = lg.nn2na(NN) 
c = np.array([  10,   20,   10,   10,   10,   30])
u = np.array([None, None, None, None, None, None])
l = np.array([   0,    0,    0,    0,    0,    0])
b = np.array([  10,   20,   15,  -25,  -20])

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

print('\n SOLVING PROBLEM WITH SIMPLEX')
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method='simplex')
print('\t Solution to the problem:')
print('\t     The raw solution will be: %s' % res.x)
for k in range(0, len(res.x)):
    if res.x[k] > 0:
        print('\t\t %d units must be moved across %s arc.' 
            % (res.x[k], str(lg.convert_arc(arcs[k], nodes))))
print('\t   The minimum cost will be: %0.2f ' % res.fun)
