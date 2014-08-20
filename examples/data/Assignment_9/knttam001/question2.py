"""program to reformat a text file so all lines are a given length
Tamsin Kantor
May 2014"""

import textwrap 

input_filename = input("Enter the input filename:\n")
output_filename = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))

# open the input file
f = open (input_filename, "r")
text = f.read()
if text.count("\n\n") > 0: # if the input file has paragraphs
    paragraphs = text.split("\n\n") # covert the text into seperate strings             
f.close() # close the input file

if text.count("\n\n") > 0: # for a file that has paragraphs
    text = []
    for x in paragraphs: 
        sentence = textwrap.wrap(x,line_width) 
        text += sentence
        text += " " # add a space between paragraphs
else: # for a file that has no paragraphs
    text = textwrap.wrap(text,line_width)

# open the output file 
g = open(output_filename, "w")
for i in text: 
    print(i, file = g)
g.close() # close the output file