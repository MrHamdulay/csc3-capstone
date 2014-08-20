"""Assignment 9-Q2
Annika brundyn
12/05/14"""

#get input from user
inputfile = input("Enter the input filename:")
outputfile = input("Enter the output filename:\n")
linewidth = input("Enter the line width:\n")
linewidth = int(linewidth)


#open file
infile = open(inputfile, "r")
lines = infile.read()

#close file
infile.close()