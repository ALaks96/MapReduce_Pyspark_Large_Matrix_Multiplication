#!/usr/bin/env python

import sys   

length = 2
width = 2

#length = int(200) + 1
#width = int(200) + 1

for line in sys.stdin:
	matrix, row, col, val = line.rstrip().split(",")
	if matrix == "A":
		for i in range(0,length):
			key = "A" + str(i)
			if row == str(i):
				print("%s\t%s\t%s"%(key,col,val))
	if matrix == "B":
		for i in range(0,width):
			key = "B" + str(i)
			if col == str(i):
				print("%s\t%s\t%s"%(key,row,val))
