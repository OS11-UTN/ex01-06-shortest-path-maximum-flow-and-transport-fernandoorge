##############################################################################
#	OS11 LOGISTICS
#	Author: Orge, Fernando Gabriel
#	EX2
#		Basic Example of Shortest Path Problem
#		with different algorithms
#
#	Solution:
#		This new graph has the same NN matrix as the previous one, hence,
#		it can be model as follows
# 		NN = np.array( [[0, 1, 1, 0, 0, 0],
#               		[0, 0, 0, 1, 0, 1],
#               		[0, 0, 0, 0, 1, 0],
#               		[0, 0, 0, 0, 0, 1],
#               		[0, 0, 0, 0, 0, 1],
#              	 		[0, 0, 0, 0, 0, 0]])
#
#		However the Cost Vector is now equal to
#			C = [2,1,2,5,2,1,2] 	the cost of each arc
#
#		The X vector (decision vars) is the same
#			X = [x1,x2,...,xn]  	binary decision of taking xi path
#
#		and the RHS of the equation is also the same
#			b = [1,0,0,0,0,0,-1]	an imaginary load will be moved 
#									from node s to node t
#			A = is the node-arc matrix obtained from the node-node one
#
#       Relevant notes:
#           the interior-point method is not able to find a solution.
#           the simplex algorithm gives us the optimal solution.
#
##############################################################################
import numpy     	as 		np
from basic_utils 	import 	nn2na, get_selected_arcs
from scipy.optimize import 	linprog

NN 				= np.array([[0, 1, 1, 0, 0, 0],
                			[0, 0, 0, 1, 0, 1],
                			[0, 0, 0, 0, 1, 0],
                			[0, 0, 0, 0, 0, 1],
                			[0, 0, 0, 0, 0, 1],
                			[0, 0, 0, 0, 0, 0]])
C      			= np.array([2, 1, 2, 5, 2, 1, 2])
Aeq, arc_idxs	= nn2na(NN)
beq    			= np.array([1, 0, 0, 0, 0, -1])
bounds 			= tuple([(0, None) for arcs in range(0, Aeq.shape[1])])

print('## Optimizer inputs ## \n'
      'Cost vector                   :   %s \n'
      'A_eq Node-Arc matrix          : \n%s \n'
      'b_eq demand-supply vector     :   %s \n'
      'Bounds of each X arc variable :   %s \n' % (C, Aeq, beq, bounds))

for name_method in 'interior-point', 'simplex':
    print('\n SOLVING PROBLEM WITH: %s' % name_method)
    res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method=name_method)
    selarcs = get_selected_arcs(arc_idxs, res.x)
    print('\t Solution to the problem:')
    print('\t   The raw solution will be: %s' % res.x)
    print('\t   The arcs that make the shortest path will be (from, to): %s' % selarcs)
    print('\t   The minimum cost will be: %0.2f ' % res.fun)