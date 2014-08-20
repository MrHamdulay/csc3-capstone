#Assignment 9 - Question 2
#Reformats text file to given length
#Aidan de Nobrega DNBAID001
#10/05/2014

#textwrap.fill is short for ("\n".join(wrap(text, ...)))
#makes for neater code
from textwrap import fill

input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

with open(input_file, "r") as f: #read-only and closes automatically
    lines = ""
    for line in f:
        #this Boolean is here to show separate paragraphs - see line 22
        if line == "\n":
            lines += "  " 
        else:
            #whitespace and escape characters stripped
            lines += line.strip() + " "

#from lines 17-19, a 3-char space will separate string into paragraphs
#done to ensure there are no mistakes
paragraphs = lines.split("   ")

formatted_paragraphs = []

#paragraphs are formatted to have width specified above
for paragraph in paragraphs:
    formatted_paragraphs.append(fill(paragraph, width))
    
formatted_string = ""

#paragraphs are concatenated with new lines appended after each
for paragraph in formatted_paragraphs:
    formatted_string += paragraph + "\n\n"

#write-only
#entire string written to output file and closed automatically
with open(output_file, "w") as out:
    out.write(formatted_string)
        
    
    
        