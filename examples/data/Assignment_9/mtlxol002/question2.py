"""CSC1015F Assignment 9 Question 2
Xola Matlanyane MTLXOL002
20 May 2014"""

import textwrap
inpfilenm = input("Enter the input filename:\n")   #ask for an input file
outpfilenm = input("Enter the output filename:\n")   #ask for an output file
linewidth = eval(input("Enter the line width:\n"))     #ask for width of line (for paragraph block)
file = open(inpfilenm, "r") #open the file in order to read it
fr = file.read() #read the file
file.close()  #close the file
#textwrapping begins
newfile = open(outpfilenm, "w") 
lst=textwrap.wrap(fr,width=linewidth)
for i in lst:
    print(i,file=newfile)
newfile.close()