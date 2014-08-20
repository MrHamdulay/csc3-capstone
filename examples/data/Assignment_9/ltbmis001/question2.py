"""programme to edit files and save as new files
mishka latib
16 may 2014"""

#gets inputs

file = input("Enter the input filename:\n")
new_file = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))

#opens file

f = open(file, "r")
lines = f.readlines()
f.close()

#puts info in correct form
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]
    lines[i] = lines[i] + " "

single_str = "".join(lines)
single_list = single_str.split(" ")
single_list.append(" "*100)

#creats list
new_line = ""
new_list = []

for i in range(len(single_list)-1):
    new_line = new_line + single_list[i] + " "
    if (len(new_line) + len(single_list[i+1])) >= line_width:
        new_list.append(new_line)
        new_line = ""
        
for i in range(len(new_list)):
    new_list[i] = new_list[i][:-1]
    
#opens file to overwrite
fn = open(new_file, "w")

#edits file
for i in new_list:
    print(i, file=fn)
    
#closes file
fn.close()