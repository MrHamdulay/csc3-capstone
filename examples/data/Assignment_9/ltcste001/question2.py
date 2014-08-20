#Stephanie Latchmanan
#Assignment 9 (reformat textfile)
#10 may 2014
import textwrap

#input the filename from user
filename = input("Enter the input filename:\n")
#open the file and read into array lines
f = open(filename, "r")
lines = f.read()
#close the file
f.close()

#split paragaphs based on double newlines
if lines.count("\n\n") != 0:
    lines = lines.split("\n\n")


#get the output file name and the width of the outputed lines
output = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

newlines = []
#if no paragraphs
if lines.count("\n\n") == 0 :
    newlines = textwrap.wrap(lines,width)
#if lines has paragraphs
else:
    for paragraph in lines:
        line = textwrap.wrap(line,width)
        newlines += (line + " ")

#open the file for the output
output_file = open(output,"w")
for line in newlines:
    print(line, file = output_file)
#close the output file
output_file.close()