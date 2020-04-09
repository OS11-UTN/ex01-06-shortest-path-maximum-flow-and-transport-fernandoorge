import numpy as np

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
            

def nn2na(NN):
    """Return Node-Arcs matrix based on Node-Node Matrix."""
    # Input  : NN  Node-Node Matrix
    # Output : NA  Node-Arc  Matrix
    (row, col) = NN.shape
    elem = count_ones(NN)
    NA   = np.zeros((row, elem))
    k    = 0
    for i in range (0, row):
        for j in range (0, col):
            if (NN[i,j] == 1):
                NA[i,k] = +NN[i,j]
                NA[j,k] = -NN[i,j]
                k       = k + 1
    return NA