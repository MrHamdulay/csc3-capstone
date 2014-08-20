import textwrap

file_in = input("Enter the input filename:\n")
file_out = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open(file_in, "r")
lines = f.read()
f.close()

lines = lines.split("\n\n")

x = open(file_out, "w")
for i in range(len(lines)):
    line = textwrap.wrap(lines[i], width)
    for j in line:
        print(j, file=x)
    print(file=x)
x.close()