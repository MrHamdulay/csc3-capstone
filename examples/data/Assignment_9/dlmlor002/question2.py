"""program to reformat a text file so that all lines are at most a given length
Lorena Dal Maso
14 May 2014"""

import textwrap

filename = input("Enter the input filename:\n")
new_file = input("Enter the output filename:\n")
line_width = input("Enter the line width:\n")

f = open(filename,"r")

value = f.read()

list = textwrap.wrap (value, width = eval(line_width))

f.close()

g = open(new_file,"w")

for element in list:
    print (element, file = g)
    
g.close()