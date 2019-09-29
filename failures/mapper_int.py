import sys
import string
import numpy
#Split line into array of entry data
for line in sys.stdin:
    entry = line.split("\t")
# Set row, column, and value for this entry
    row = int(entry[1])
    col = int(entry[2])
    value = float(entry[3])

#If this is an entry in matrix A...
    if (entry[0] == "A"):
    
    #Generate the necessary key-value pairs
        for i in range(col):
            print('<{}{},{} {} {}}>'.format(row,i,A,col,value))
#Otherwise, if this is an entry in matrix B...
    else:
    #Generate the necessary key-value pairs
        for i in range(row):
            print('<{}{},{} {} {}}>'.format(i,col,B,row,value))
