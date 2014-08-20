#Thembekani Gwegwana
#16 May 2014
#A program to modify a file length

#Input fron user
input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
#Overwring and reading files
g = open(output_file, "w")
f = open(input_file, "r") 
lines = f.readlines()
f.close() 

total_char = 0
for i in range(len(lines)):
    total_char += len(lines[i])

total_lines = (total_char+41)//width

for i in range(total_lines):
    if len(lines[i]) < width:
        print(lines[i], file = g) 
    else:
        print(lines[i][:lines[i][0:width].rfind(" ")].strip(), file = g)
    lines.append("") 
    
    if "\n" in lines[i]: 
        lines[i+1] = lines[i][lines[i][0:width].rfind(" ")+1:lines[i].rfind("\n")] + " " + lines[i+1] 
    else:
        lines[i+1] = lines[i][lines[i][0:width].rfind(" ")+1:] + " " + lines[i+1]
g.close()


