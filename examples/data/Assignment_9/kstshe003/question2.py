#sheldon kisten
#15 may 2014
#question 2

import textwrap

infilename=input("Enter the input filename:\n")
f=open(infilename, "r")
x=f.read()
f.close()

outfilename=input("Enter the output filename: \n")
g=open(outfilename, "w")
width=int(input("Enter the line width: \n"))

if width>=0:
    pass    
else:
    width=40
    
print(textwrap.fill(x, width), file=g, end="")
g.close()
