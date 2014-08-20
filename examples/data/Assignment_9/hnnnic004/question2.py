'''program to format file line length
nicole henning
due 16 may 2014'''

import textwrap

file1 = input("Enter the input filename:\n")
infile = open (file1, "r") #opens, read, and closes file = filename
lines = infile.read () 
infile.close()

file2 = input("Enter the output filename:\n") #creating output file
outfile = open (file2, "w") #overwrite output file

width = eval(input("Enter the width:\n"))
lines2 = textwrap.wrap(lines,width) #sets width

for i in lines2:
    print (i, file = outfile) #print to output file
outfile.close()
