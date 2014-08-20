#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     reformats a text file to shorten lines to a given length
#
# Author:      Matthias
#
# Created:     11-05-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

input_name = input("Enter the input filename: \n")
input_content = open(input_name, "r")
data_list = input_content.readlines()
input_content.close()

output_name = input("Enter the output filename: \n")
output_content = open(output_name, "w")

width = eval(input("Enter the line width: \n"))

word_list = []

for line in data_list:
    word = ""
    if line == "\n":
        # indicates an empty line - new paragraph
        # append an empty string to indicate this
        word_list.append("")
    else:
        for i in range(len(line)):
            if line[i] == " ":
                # seperate into a new word and add a space
                word_list.append(word + " ")
                word = ""
            else:
                # add current character to word
                word += line[i]
        # append the last word (without \n, but with a space)
        word_list.append(word.strip()+" ")

line_length = 0
line_string = ""

for word in word_list:
    if word == "":
        # empty string indicates new paragraph
        print(line_string, file = output_content)
        print(file = output_content)
        line_string = ""
        line_length = 0
    elif line_length + len(word)-1 <= width:
        # The line is not yet full
        # len(word) - 1 to negate the space at the end of the word
        line_length += len(word)
        line_string += word
    else:
        # The line is full - print and reset the counters
        print(line_string, file = output_content)
        line_length = len(word)
        line_string = word

# print the rest of the last line
print(line_string, file = output_content)

output_content.close()