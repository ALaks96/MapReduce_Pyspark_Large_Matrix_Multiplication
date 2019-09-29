#!/usr/bin/python


import sys
import string
import numpy

current_row_A = 0
current_row_B = 0
k = 0
i = 0

#A,0,0,0.0
#A,0,1,1.0
#A,1,0,2.0
#A,1,1,3.0
#B,0,0,1.0
#B,0,1,2.0
#B,1,0,3.0
#B,1,1,4.0

for line in sys.stdin:
    
    line = line.strip()
    
    #Split line into array of entry data
    element = line.split(" \\cf")
    
    
    # Set row, column, and value for this entry
    
    print(element)
