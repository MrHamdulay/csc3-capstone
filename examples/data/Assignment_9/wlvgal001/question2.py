"""Question 2: A program that makes a given file all the same given length
Galya Wolov
16 may 2013"""

import textwrap #imports the built in function textwrap to use in later code


#opens the file which is inputted then reads it using the 'r' mode and then closes it
inputfile=open(input("Enter the input filename:\n"), "r")
lines=inputfile.read() #reads the entire file in one long line with \n as breaks
inputfile.close() #closes file

#all the inputs 
output_file= input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
eachline= textwrap.wrap(lines, width=width) #this uses the textwrap built in function's wrap which forces each line of the file into the inputted width length 

#opens the file which will be outputted then overwrites it using the 'w' mode and then closes it
outputfile=open(output_file, 'w')
for i in eachline: #iterates through each line of wrapped above and through the file= outputfile prints it in the new file and not in this current program
    print(i, file=outputfile) #by saying file=outfile, it means that python will print it in the outfile and not on the dialog
outputfile.close() #closes file





