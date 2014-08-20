"""Bella Gorham
line seperator and writer to a certain amount of cahracters per line
15/05/14"""


#inputs
file_in = input("Enter the input filename:\n")

file_out = input("Enter the output filename:\n")

width = eval(input("Enter the line width:\n"))

# recrusive function to sep lines but not split words
def output(lines):
    if len(lines) < width:
        return lines
    else:
        return lines[0:(lines[0:width +1].rfind(" "))] + "\n" + output(lines[(lines[0:width+1].rfind(" "))+1:])     

f = open(file_in,"r")
lines = f.read()
f.close()
lines = lines+" "


# taking into account paragraphs
if "\n\n" in lines:
    lines = lines.split("\n\n")

# account for one item in the list
if type(lines) == list:
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n"," ")
else:
    lines = lines.replace("\n"," ")

# write to new file
g = open (file_out, "w")
if type(lines) == list:
    for i in range(len(lines)-1):
        print(output(lines[i]) + "\n", file = g)
    print(output(lines[len(lines)-1]), file = g)
else:
    print(output(lines), file = g)
g.close ()