'''Siphesihle Zwane
text length editor
15/05/14'''

infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

g = open(outfile, "w")
f = open(infile, "r") 
lines = f.readlines()
f.close() 

char = 0
for i in range(len(lines)):
    char += len(lines[i])

total_lines = (char+width-1)//width

for i in range(total_lines):
    if len(lines[i]) <= width:
        print(lines[i], file = g) 
    else:
        print(lines[i][:lines[i][0:width].rfind(" ")].strip(), file = g)
    lines.append("") 
    
    if "\n" in lines[i]: 
        lines[i+1] = lines[i][lines[i][0:width].rfind(" ")+1:lines[i].rfind("\n")] + " " + lines[i+1] 
    else:
        lines[i+1] = lines[i][lines[i][0:width].rfind(" ")+1:] + " " + lines[i+1]
g.close()


