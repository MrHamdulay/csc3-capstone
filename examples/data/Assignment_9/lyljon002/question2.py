#10 May 2014   
#Program to reformat a file to max length per lines
#LYLJON002

import textwrap

inputname = input("Enter the input filename:\n")
outputname = input("Enter the output filename:\n")          #get all names and values
width = eval(input("Enter the line width:\n"))

f = open(inputname)
contents = f.read()
f.close()



output = textwrap.fill(contents, width)     #wrap the text
print(output)



with open(outputname, "w") as text_file:        #output the text
    text_file.write(output)