"""Question 2-Assignment 9
FRNHAN004
13 May 2014"""

import textwrap 

file_i=input("Enter the input filename:\n")
file_o=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n")) #width input

f1=open(file_i, "r") #open file to be read
lines=f1.read()
f1.close() #close file!

line= textwrap.wrap(lines, width=width) #textwrap.wrap fixes the width to the width you want


f2=open(file_o, 'w')#open file to be written
for i in line:
    print(i, file=f2) 
f2.close()#close the file!