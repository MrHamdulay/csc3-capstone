"""
Align Text to a given length
Keyoolin Padayachee
15 May 2014
"""
import textwrap #import Textwrap module

#Get inputs
Input = input("Enter the input filename:\n")
Output = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#Reads and saves the lines from a text file
marks = open (Input, "r")
lines = marks.read()
marks.close()
paragraph = lines.split("\n\n")
#Wraps the text to a given width
text = []
for i in range(len(paragraph)):
    text.append([])
    text[i] = textwrap.wrap(paragraph[i],width)
#Writes the text to an output file
output = open(Output, "w")
for i in range(len(text)):
    for j in range(len(text[i])):
        print(text[i][j], file = output)
    print(" ", file = output)
output.close()

