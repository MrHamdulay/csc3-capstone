"""program to print file to another file with spesific line witdh
herman claassens
15 may 2014"""

import textwrap    # use textwrap function
the_file=input("Enter the input filename:\n")
result=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

# access information in files by opening them
f=open(the_file)
text=f.read()
f.close()

#creates changed file
output=textwrap.fill(text, width)

#prints out changed file
with open(result, "w") as text_file:
    text_file.write(output)