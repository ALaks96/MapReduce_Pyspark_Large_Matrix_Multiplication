#!/usr/bin/python

import sys
import numpy as np

# We know the dimensions of A and B!
length = int(200) + 1
width = int(200) + 1

# Initializing A_list and B_list to deal with sparsity
A = [0]*(length*width)
B = [0]*(length*width)

for line in sys.stdin:
    
    # Retrieving elements of (key,value) pair of our map output
    lines = line.strip()
    element = lines.split("\t")
    
    # The provenance of the element and its row/column
    origin = element[0]
    
    # The intermediate index to keep the order within the original matrix
    index = int(element[1])
    
    # The value associated to that element:
    val = int(element[2])
    
    for i in range(0,201):
        if origin == "A" + str(i):
            A[length*i + index] = val
            print '%s\t%s' % (origin,val)
                
        if origin == "B" + str(i):
            B[width*i + index] = val
            print '%s\t%s' % (origin,val)
