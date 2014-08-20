

import textwrap

#Obtaining input and output files and line width
infile = input ("Enter the input filename:\n")
outfile = input ("Enter the output filename:\n")
width = eval (input ("Enter the line width:\n"))

#Open file and storing file in string
f = open (infile, "r")
x = f.read ()
f.close ()

#Wrapping text to provided length
if x.find ("\n\n") != -1:
    z = x.split ("\n\n")
    for i in z:
        y = textwrap.wrap (i, width = width)
        print ("\n")
else:
    y = textwrap.wrap (x, width = width)  

#Writing wrapped text to supplied output file
f = open (outfile, "w")
for i in y:
    print (i, file = f)
f.close ()
        