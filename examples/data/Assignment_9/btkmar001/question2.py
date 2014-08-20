# A program that limits line length in a text file without splitting words, and then writes the textwrapped content to a new file
# Martin Batek
# BTKMAR001
# 13 May 2014

import textwrap # For text wrapping function

filename1 = input("Enter the input filename:\n")
filename2 = input("Enter the output filename:\n")
lengthofline=eval(input("Enter the line width:\n"))
# Gather input filename, output filename, and line width from user
inf = open(filename1,"r")
filecontent = inf.read()
inf.close()
# Open input file, store its contents into a varible, close input file

filecontent = filecontent.split("\n\n") # Split up paragraphs

for i in range(len(filecontent)):
    filecontent[i] = textwrap.wrap(filecontent[i],width=lengthofline)
# Changes filecontent into a list of strings that are equal to or less than the specified character length    

outf = open(filename2,"w")
# Open new/already existing output file
for i in range(len(filecontent)):
    for line in filecontent[i]:
        print(line, file = outf)
    print(file = outf) # Ensures that an extra linebreak is printed between paragraphs
# Print each line of filecontent to output file to file content    
outf.close()
# Close output file    