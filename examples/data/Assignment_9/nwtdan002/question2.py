'''Program to change the width of lines of text
By Daniel Newton
10/05/14'''

import textwrap

file=input("Enter the input filename:\n")
result=input("Enter the output filename:\n")
w=eval(input("Enter the line width:\n"))

f=open(file)
text=f.read()
f.close()

output=textwrap.fill(text, w)

with open(result, "w") as text_file:
    text_file.write(output)