"""Assignment 9 Question 2
James Lloyd
10 May 2014"""

import textwrap
infile = input ("Enter the input filename:\n")
outfile = input ("Enter the output filename:\n")
width = eval (input ("Enter the line width:\n"))

f = open (infile, "r")
x = f.read ()
f.close ()


y = textwrap.wrap (x, width = width)

f = open (outfile, "w")
for i in y:
    print (i, file = f)
f.close ()
        