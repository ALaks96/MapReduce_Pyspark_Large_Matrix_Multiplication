#!/usr/bin/python

import sys
import numpy as np

length = int(200) + 1
width = int(200) + 1

for line in sys.stdin:
    
    # Retrieving output from second mapper:
    lines = line.strip()
    element = line.split('\t')
    origin = element[0]
    
    # Reattributing lists:
    
    while A_list & B_list:
        if origin == "A":
            A_list = element[1]
    
        if origin == "B":
            B_list = element[1]

print(A_list)
print(B_list)
#
#    # If both lists were recovered proceed to computation (this is the lack of parallelism):
#    if A_list != [] & B_list != []:
#        
#        for i in range(0,length):
#            for j in range(0,width):
#        
#                # Retrieving line i of A and column j of B
#
#                C_A= np.array(A_list[length*i : length*(i+1)])
#                C_B = np.array(B_list[width*j : width*(j+1)])
#    
#                #Computing element-wise product of elments of line i of A and column j of B
#                C_temp = C_A * C_B
#        
#                # Summing the product to yield element i,j of C!
#                C = np.sum(C_temp)
#                print '%s\t%s' % ((i,j),C)
#
##Again for more transparancy have a look a this output rather than the above! (uncomment)
## print '%s\t%s\t%s\t%s\t%s' % (i,j,C,my_row,my_col)
