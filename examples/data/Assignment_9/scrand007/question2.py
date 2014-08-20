inp = input("Enter the input filename:\n")
outp = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
def output(lines):
    if len(lines) < width:
        return lines
    else:
        return lines[0:(lines[0:width +1].rfind(" "))] + "\n" + output(lines[(lines[0:width+1].rfind(" "))+1:])     

f = open(inp,"r")
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


g = open (outp, "w")
if type(lines) == list:
    for i in range(len(lines)-1):
        print(output(lines[i]) + "\n", file = g)
    print(output(lines[len(lines)-1]), file = g)
else:
    print(output(lines), file = g)
g.close ()