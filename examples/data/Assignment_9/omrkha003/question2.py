# program to reformat a text file so that all lines are at most a given length
# khadeejah omar
# 14 may 2014

import textwrap

input_file = input("Enter the input filename: \n")
output_file = input("Enter the output filename: \n")
line_width = eval(input("Enter the line width: \n"))

# read lines from input file as a single string
input_f = open(input_file, "r")
file_string = input_f.read()
input_f.close()

# remove newline characters from string
new_file_str = ""
for character in file_string :
    if character != "\n" :
        new_file_str += character
    else :
        new_file_str += " "

# reformat the string according to line width        
new_file_list = textwrap.wrap(new_file_str, width = line_width)

# write the formatted lines to the output file
output_f = open(output_file, "w")
for value in new_file_list :
    print(value, file = output_f)