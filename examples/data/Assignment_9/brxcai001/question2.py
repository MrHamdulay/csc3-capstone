#Program to reformat a textfile so that all lines are at most a given length.
#BRXCAI001
#16 May 2014

#Import textwrap. A built-in module with functions.
import textwrap

#Assign variables to inputs.
inputfilename = input("Enter the input filename:\n")
outputfilename = input("Enter the output filename:\n")

widthlen = input("Enter the line width:\n")

#Open input file and convert each line into a string in a list. Close file.
inputfile = open(inputfilename, "r")
lines = inputfile.read()
inputfile.close()

#Textwrap is a function that adjusts the width for a given parameter. Make this parameter equal to the input width.
format_line = textwrap.wrap(lines, width=widthlen)

#Open the output file and write over it.
outputfile = open(outputfilename, "w")

for i in format_line:
    print (i, file=outputfile)

#Close file.
outputfile.close()
