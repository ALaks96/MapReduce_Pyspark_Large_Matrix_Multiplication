#!/usr/bin/python



import sys

# input comes from STDIN (standard input)


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    element1 = line.split(',')
    c = 0
    
    for element in element1:
        c += 1
        if c == 1:
            print (element1)

        else:
            
            continue