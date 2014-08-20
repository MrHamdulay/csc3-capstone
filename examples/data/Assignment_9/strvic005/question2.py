"""program to reformat a text file so that all lines are at most a given length
vicky stark
14 may 2013"""

import textwrap #textwrap is a built-in module with functions

#assign variables to the inputs
in_file=input("Enter the input filename:\n")
out_file=input("Enter the output filename:\n")
w=eval(input("Enter the line width:\n")) #width input

#open the input file and put the lines into one string, then close file
infile=open(in_file, "r")
lines=infile.read()
infile.close()

line= textwrap.wrap(lines, width=w) #textwrap.wrap adjusts the width, and it has a parameter 

#open the output file, write over it, close it 
outfile=open(out_file, 'w')
for i in line:
    print(i, file=outfile) #by saying file=outfile, it means that python will print it in the outfile and not on the dialog
outfile.close()