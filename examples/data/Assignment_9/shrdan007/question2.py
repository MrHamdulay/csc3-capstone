# Text reformatting
# Danielle Sher

import textwrap

x = input("Enter the input filename:\n")
y = input("Enter the output filename:\n")
z = eval(input("Enter the line width:\n"))


a = open(x, "r")

b = a.read()


lst = textwrap.wrap(b, width = z)

string = "\n".join(lst)

c = open(y, "w")
c.write(string)

a.close()
c.close()
