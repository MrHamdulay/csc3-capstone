"""Keegan Naidoo
NDXKEE009
10 May 2014
Program to wrap text in textfile"""

file_input = input("Enter the input filename:\n")              #Inputs filenames and width of lines 

file_output = input("Enter the output filename:\n")

width = eval(input("Enter the line width:\n"))

f = open (file_input,"r")                                     #Opens file to read from

lines = f.read()                                              #Stores the text in a string variable

import textwrap                                               #Imports wrap function for use

wrap = textwrap.wrap(lines, width)                            #Wraps lines with width

file_output2 = open(file_output,"w")                         #Opens file to write to

for line in wrap:                                             #Writes text to output file
    print(line, file = file_output2)

f.close()