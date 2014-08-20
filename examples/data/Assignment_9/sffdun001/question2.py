"""Question 2- Assignment 9: editing the width of text in a file
Duncan Saffy
14 May 2014"""

import textwrap

#Retrieving inputs
infile = input('Enter the input filename:\n')
outfile = input('Enter the output filename:\n')
w = eval(input('Enter the line width:\n'))

#getting info from infile
file_a = open(infile,'r')
lines=file_a.read()
file_a.close()

p = textwrap.wrap(lines, width=w)

# creating new file with adjusted text
file_b = open(outfile, 'w')
for i in p:
  print(i, file=file_b)
file_b.close()
