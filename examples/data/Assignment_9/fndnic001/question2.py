'''reformating a file to specified width
nic findlay
10 may 2014'''
#getting the file contents

file_name = input('Enter the input filename:\n') 
out_file_name = input('Enter the output filename:\n')

f = open(file_name,'r')  #opening input file 
lines = f.read()
f.close()

new_lines = []   #two arrays
used_lines = []

width = eval(input('Enter the line width:\n'))

for line in lines:   #removing \n from the end
    if line[-1] == '\n':
        new_lines.append(line[:-1])
    else:
        continue  #new_lines puts lines into list
    
new_lines = lines.split()  #all words in text file into list
combo_line = ''


for i in range(len(new_lines)):   #making lines into format of width
    if len(combo_line + new_lines[i])  < width:
        combo_line += new_lines[i] + ' '
        
    else:
        used_lines.append(combo_line)
        combo_line = new_lines[i] + ' ' 
        

out_file = open(out_file_name, 'w')  #printing to output file
for i in used_lines:
    print(i, file = out_file)
print(combo_line, file = out_file)
out_file.close()



        
    

    

        