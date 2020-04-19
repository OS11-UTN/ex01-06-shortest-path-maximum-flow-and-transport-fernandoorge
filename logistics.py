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

def count_non_zeros(NN):
    """Return number of non-zero elements in Node-Node Matrix."""
    # Input  : NN   Node-Node Matrix
    # Output : int  number of ones in NN Matrix
    (row, col) = NN.shape
    elem       = 0
    for i in range (0, row):
        for j in range (0, col):
            if (NN[i,j] > 0):
                elem = elem + 1
    return elem

def nn2na(NN):
    """Return Node-Arcs matrix based on Node-Node Matrix."""
    # Input  : NN       Node-Node Matrix
    # Output : NA       Node-Arc  Matrix
    # Output : arcs     arcs      list of tuples
    (row, col) = NN.shape
    elem = count_ones(NN)
    NA   = np.zeros((row, elem))
    k    = 0
    arcs = []
    for i in range (0, row):
        for j in range (0, col):
            if (NN[i,j] == 1):
                NA[i,k] = +1
                NA[j,k] = -1
                k       = k + 1
                arcs.append((i, j))
    return NA, arcs

def convert_arc(arc, nodes):
    """Return an equivalent arc but with names instead of integer values."""
    # Input  : arc      Tuple of integer values
    # Input  : nodes    list of Nodes names as string values
    # Output : carc     Converted Arc => Tuple of strings
    #
    # NOTES  : This function is used just for printing results 
    #          and for debugging purposes
    return (nodes[arc[0]], nodes[arc[1]])

def convert_path(path, nodes):
    """Return an equivalent path but with names instead of integer values."""
    # Input  : path     path as list of nodes
    #                   Nodes are assumed to be integer values
    # Input  : nodes    list of all nodes names in the graph
    #                   Nodes are assumed to be string values
    # Output : cpath    Converted path => list of strings
    #
    # NOTES  : This function is used just for printing results 
    #          and for debugging purposes
    cpath = []
    for k in range(0,len(path)):
        cpath.append(nodes[path[k]])
    return cpath
    
def dijkstra_alg(NN, nodes):
    """DIJKSTRA Algorithm"""
    # Input  : NN       Node-Node Matrix
    # Input  : nodes    list of all nodes names in the graph
    #                   Nodes are assumed to be string values
    # NOTES  : This function prints all the results
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
    

def get_path_as_string(arcs, vec):
    msg = ''
    for k in range(0, len(arcs)):
        if vec[k] == 1:
            msg = msg + '(' + arcs[k] + ')'
    return msg
    
def dfs(G, i, j):
    """."""
    (row, col) = G.shape
    label = [ 0 for col in range(row)]
    pred  = [-1 for col in range(row)]
    path  = []
    s     = []
    s.insert(0,i)
    while (len(s) != 0):
        v = s.pop()
        if (label[v] == 0):
            label[v] = 1
            for arc in get_arcs_from_node(G, v):
                pred[arc[1]] = v
                s.insert(0,arc[1])
    if (label[j] == 0):
        print('\tERROR: Path not found!')
    else:
        path.insert(0, j)
        while (label[j] == 1 and pred[j] >= 0):
            j = pred[j]
            path.insert(0, j)
    return path

# def dfs_at_na(NA, i, j):
#     """."""
#     (nodes, arcs) = NA.shape
#     label = [ 0 for col in range(nodes)]
#     pred  = [-1 for col in range(nodes)]
#     path  = []
#     s     = []
#     s.insert(0,i)
#     while (len(s) != 0):
#         v = s.pop()
#         if (label[v] == 0):
#             label[v] = 1
#             for arc in range(0, arcs):
#                 if NA[v, arc] > 0:
#                     pred[arc] = v
#                     s.insert(0,arc)
#     if (label[j] == 0):
#         print('\tERROR: Path not found!')
#     else:
#         path.insert(0, j)
#         while (label[j] == 1 and pred[j] >= 0):
#             j = pred[j]
#             path.insert(0, j)
#     return path

def residualg(G):
    (row, col) = G.shape
    for i in range(0, row):
        for j in range(0, col):
            if G[i,j] < 0:
                G[i,j] = 0
    return G

def max_flow_across_path(path, G):
    """@TODO"""
    c = []
    for k in range(0, len(path)-1):
        i = path[k]
        j = path[k+1]
        c.append(G[i,j])
    return min(c)

def nn2nac(NN, nodes, costs):
    """@TODO"""
    NA, arcs = nn2na(NN, nodes)
    NAC = na2nac(NA, costs)
    return NAC

def na2nac(NA, costs):
    """@TODO"""
    (row, col) = NA.shape
    NAC        = np.zeros((row, col))
    for i in range (0, row):
        for j in range (0, col):
            NAC[i,j] = NA[i,j] * costs[j]
    return NAC
