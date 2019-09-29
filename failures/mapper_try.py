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
    element = line.split(" ")

# Set row, column, and value for this entry

    print(element)

    provenance = element[0]
    row = int(element[1])
    col = int(element[2])
    value = float(element[3])

#If this is an entry in matrix A...
    if (provenance == "A"):
        
        if current_row_A == row:
            k += 1
            # print('<{}{},{} {} {}}>'.format(i,A,col,value))
            print '%s\t%s' % ((row,k),(provenance, col, value))
                
        else:

            k = 0
            current_row_A = row
            print '%s\t%s' % ((row,k),(provenance, col, value))

#Otherwise, if this is an entry in matrix B...
    else:
        
        if current_row_B == row:
            
            i += 1
            print '%s\t%s' % ((i,col),(provenance, row, value))
            # print('<{}{},{} {} {}}>'.format(i,col,B,row,value))

        else:

            i = 0
            current_row_B = row
            print '%s\t%s' % ((i,col),(provenance, row, value))
