""" A program to reformat a text file so that all lines are at most a given length
Author: Emiel Zyde
Date: 10 May 2014 """

import textwrap 

#prompt the user for an input filename, an output filename, width 
input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#we want to read the lines in the original file
original_file = open(input_file, "r")
input_lines = original_file.read()
original_file.close()

#we need to keep the paragraphs in place and we know that paragraphs occur where there is a double newline character
if "\n\n" in input_lines:
    input_lines = input_lines.split("\n\n") 
    
#wraps the lines 
file2 = open(output_file, "w")
if type(input_lines) == list:
    for i in range(len(input_lines)):
        i = textwrap.wrap(input_lines[i], width = width)
        for line in range(len(i)-1):
            print(i[line], file = file2)   
        for line in range(len(i)-1, len(i)):     
            print(i[line], end = "\n\n", file = file2)  #putting in the end = "" character avoids the addition of an extra new-line at the paragraph split 
else:  
    i = textwrap.wrap(input_lines, width = width)
    for line in range(len(i)):
        print(i[line], file = file2)
    
file2.close()
