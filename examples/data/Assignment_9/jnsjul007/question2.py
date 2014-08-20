#Julian van Rensburg
#Assignment 9 question 2
#16 May 2014


#import function from python

import textwrap

#obtain input file from user, open file to read and close file
filename=input("Enter the filename:\n")
FILE = open (filename, "r")
lines = FILE.read()
FILE.close ()

#obtain output file name, specify line lengths and write to outputfile
outputfile= input("Enter the output filename: \n")
linewidth= eval(input("Enter the line width: \n"))

g= open(outputfile,"w")
print(textwrap.fill(lines,linewidth), file=g)

#close file
g.close()