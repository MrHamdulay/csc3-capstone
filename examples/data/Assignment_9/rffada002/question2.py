"""11/05/2014 RFFADA002 Adam Ruff
Assignment 9 Question 2
Reformat text file so that all lines are a set length and continue on the next line if that length is exceeded"""

file_in = input("Enter the input filename:\n")

file_out = input("Enter the output filename:\n")

width = eval(input("Enter the line width:\n"))


def output(lines):
    if len(lines) < width:
        return lines
    else:
        return lines[0:(lines[0:width +1].rfind(" "))] + "\n" + output(lines[(lines[0:width+1].rfind(" "))+1:])     

f = open(file_in,"r")
lines = f.read()
f.close()
lines = lines+" "

if "\n\n" in lines:
    lines = lines.split("\n\n")

if type(lines) == list:
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n"," ")
else:
    lines = lines.replace("\n"," ")


g = open (file_out, "w")
if type(lines) == list:
    for i in range(len(lines)-1):
        print(output(lines[i]) + "\n", file = g)
    print(output(lines[len(lines)-1]), file = g)
else:
    print(output(lines), file = g)
g.close ()