"""program for writing a text in a paragraph of set width
Jacqueline Blomendahl
13 May 2014"""

import textwrap

#getting inputs
input_file= input("Enter the input filename:\n")
output_file= input("Enter the output filename:\n")
width= eval(input("Enter the width:\n"))

# using the iinput file
in_file=open(input_file, "r")
file= in_file.read()
in_file.close()

#using the output file
outfile=open(output_file, "w")
x = textwrap.wrap(file, width)
for i in x:
    print(i, file=outfile)

outfile.close()