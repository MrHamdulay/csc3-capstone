'''Program to fornat a textfile
   Denzel Ncube
   10 May 2014'''

import textwrap
#Getting input for files
inp = input("Enter the input filename:\n")
outp = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#Initialising list
lst = []

#Reading file
finput = open (inp,"r")
foutput = open (outp,"w")
string = finput.read()

#Splitting file into different paragraphs
lst = string.split("\n\n")
#Wrapping each different paragraph then writing to  the new file
for i in range(len(lst)):
    newstring = textwrap.fill(lst[i],width) +"\n\n"
    foutput.write(newstring)
        
#Closing Files    
finput.close()
foutput.close()