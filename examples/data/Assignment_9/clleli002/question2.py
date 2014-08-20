""" Program to reformat a text file so that all lines are at most a given length. Text formatted to a new text file.
Elizabeth Cilliers
11/05/2014"""

import textwrap

#get the filenames
infileName=input("Enter the input filename:\n")
outfileName=input("Enter the output filename:\n")
#get the line width
width=eval(input("Enter the line width:\n"))

#open infile
infile=open(infileName,"r")
lines=infile.read()
infile.close()

#open outfile
outfile=open(outfileName,"w")

# use textwrap function.
list = textwrap.wrap(lines, width=width)

# Print each line.
for element in list:
    print(element,file=outfile)

#close outfile
outfile.close()
        
    
    
    

    


