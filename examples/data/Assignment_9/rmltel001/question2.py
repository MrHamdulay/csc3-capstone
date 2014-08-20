"""Program to reformat a text file so that all lines are at most a given 
Telisha Ramlall
11 May 2014"""

input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

g = open(output_file, "w") #Open file to write to 
f = open(input_file, "r") #Open file to read fromy

lines = f.readlines() #Read lines of textfile into an array
f.close() 


total_char = 0
#count total characters in the textfile
for i in range(len(lines)):
    total_char += len(lines[i])

#divide total characters by width to calculate number of lines in new textfile   
total_lines = (total_char+41)//width

for i in range(total_lines):
    #check if length of lines greater than width
    if len(lines[i]) < width:
        print(lines[i], file = g) 
    else:
        print(lines[i][:lines[i][0:width].rfind(" ")].strip(), file = g) #Print from 0 to the first space from the right of a substring width long of list at i
    lines.append("") #append new element in list to accommodate transferral of characters
    
    #append the rest of the characters of list at i to the beginning of the next element in the list
    if "\n" in lines[i]: #check whether there are any new lines so that they can be removed
        lines[i+1] = lines[i][lines[i][0:width].rfind(" ")+1:lines[i].rfind("\n")] + " " + lines[i+1] 
    else:
        lines[i+1] = lines[i][lines[i][0:width].rfind(" ")+1:] + " " + lines[i+1]
g.close()


