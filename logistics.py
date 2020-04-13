#   OS11 LOGISTICS
#   Author: Orge, Fernando Gabriel
#   logistics package
import numpy as np
import math 

def count_ones(NN):
    """Return number of ones in Node-Node Matrix."""
    # Input  : NN   Node-Node Matrix
    # Output : int  number of ones in NN Matrix
    (row, col) = NN.shape
    elem       = 0
    for i in range (0, row):
        for j in range (0, col):
            if (NN[i,j] == 1):
                elem = elem + 1
    return elem
            

def nn2na(NN, nodes):
    """Return Node-Arcs matrix based on Node-Node Matrix."""
    # Input  : NN       Node-Node Matrix
    #        : nodes    nodes names
    # Output : NA       Node-Arc  Matrix
    (row, col) = NN.shape
    elem = count_ones(NN)
    NA   = np.zeros((row, elem))
    k    = 0
    arcs = []
    for i in range (0, row):
        for j in range (0, col):
            if (NN[i,j] == 1):
                NA[i,k] = +NN[i,j]
                NA[j,k] = -NN[i,j]
                k       = k + 1
                arcs.append(nodes[i]+nodes[j])
    return NA, arcs

def na2nac(NA, costs):
    """@TODO"""
    (row, col) = NA.shape
    NAC        = np.zeros((row, col))
    for i in range (0, row):
        for j in range (0, col):
            NAC[i,j] = NA[i,j] * costs[j]
    return NAC
    
def get_arcs_from_node(NN, src):
    """@TODO"""
    # Inputs  : NN       Node-Node Matrix
    #         : src
    (row, col) = NN.shape   
    arcs = []
    for dst in range(0, col):
        if NN[src, dst] > 0:
            arcs.append((src, dst))
    return arcs


def dijkstra_alg(NN, nodes):
    """DIJKSTRA Algorithm"""
    # Inputs  : NN       Node-Node Matrix
    #         : nodes    nodes names
    (row, col) = NN.shape                                   # get NN dimensions
    n          = len(nodes)                                 # n == row == col
    if (row != col):
        print("ERROR: NN must be a square matrix")
        return
    if (n != row):
        print("ERROR: n != row")
        return

    dist  = np.zeros(n)                                     # distance vector
    pred  = np.zeros(n)                                     # predecessor vector
    label = np.zeros(n)                                     # 0=unlabeled, 1=labeled
    
    for k in range (1, n):
        dist[k] = math.inf                                  # initialization of distance vector

    for k in range (0, n):
        dist_min = math.inf                                 # restore upper bound
        i        = 0                                        # restore index
        for k in range(0, n):
            if (dist[k] < dist_min) and (label[k] == 0):    # find min distance of non-labeled nodes
                dist_min = dist[k]                          # update min distance if found
                i        = k                                # update index if found
        label[i] = 1                                        # label node when min distance found
        for arc in get_arcs_from_node(NN, i):
            j = arc[1]
            if dist[j] > (dist[i] + NN[i,j]):
                dist[j] = dist[i] + NN[i,j]                 # update distance vector
                pred[j] = i                                 # update predecessor vector

    path      = []                                          # shortest path               
    cum_dist  = []                                          # cumulative distance
    curr_node = n-1                                         # start with the last node
    path.insert(0,nodes[curr_node])                         # insert last node to path
    cum_dist.insert(0,dist[curr_node])                      # insert cumulative distance (solution)
    while (curr_node != 0):                                 # iterate till first node is reached
        pred_node = int(pred[curr_node])                    # find predecessor of current node
        path.insert(0,nodes[pred_node])                     # insert predecessor into the path
        cum_dist.insert(0,dist[pred_node])                  # update cumulative distance vector
        curr_node = pred_node                               # predeccesor is now the current node
        
    print("\t Shortest path solution: %s" % path)
    print("\t Cumulative distance   : %s" % cum_dist)
    print("\t Minimum distance      : %d" % cum_dist[-1])
    print("")
