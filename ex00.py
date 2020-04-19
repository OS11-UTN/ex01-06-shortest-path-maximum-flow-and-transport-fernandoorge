##############################################################################
#	OS11 LOGISTICS
#	Author: Orge, Fernando Gabriel
#	EX0
#		Build a function that transforms Node-Node matrix (incidence matrix) 
#		to Node-Arc matrix
#
#	Solution:
#		The function nn2na is implemented in the logistics.py file
#		As an example, an arbitrary node-node matrix M is used and 
#		the resultant Node-Arc matrix is printed
##############################################################################

import numpy     as np
import logistics as lg

nodes = ['s','2','3','t']
M = np.array( [ [0, 1, 1, 0],
                [0, 0, 1, 1], 
                [0, 0, 0, 1], 
                [1, 0, 0, 0] ])

NA, arcs = lg.nn2na(M)

print('Node-Arc Matrix: \n%s\n' % NA)
print('The following arcs were found:')
for arc in arcs:
	print('\tArc found: %s' % str(lg.convert_arc(arc, nodes)))