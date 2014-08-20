"""program to reformat a text file so that all lines are at most a given length and then rewrite it to a new text file
Brandon Pickup
11 May 2014
Assignment 9 Question2"""

in_file_name = input("Enter the input filename:\n")
out_file_name = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))
in_file = open(in_file_name,"r")
lines = in_file.readlines()#reads the entire text file into a single line
in_file.close

for i in range (len(lines)):#removes the new line characters from the end of each line
    if lines[i][-1] == "\n" and lines[i]!="\n":
        lines[i] = lines[i][:-1]

current_width = 0
new_lines = []
current_line = ""
for i in range (len(lines)):
    current = lines[i].split(" ")#breaks each line into a list of words
    for j in range (len(current)):
        current_width+= len(current[j])#adds the width of the current word to the accumulating width of the new line
        if current[j] == "\n":#special case where a line is skipped between characters, the new line character is added on its own to the formatted list
            new_lines.append(current_line)
            current_line = current[j] 
            current_width = 0
        elif current_width <= line_width:#if the length of the new line is less than the specified length of the line, add the word to that line
            current_line += current[j]
            if j != len(lines[i])-1:#only adds a space after the word if it is not the last word of the entire line.
                current_line += " "
                current_width += 1
        else:#if when the word is added to the line, the length of the line falls outside the specified requirements, the line is appended to the list of new lines, and the current word becomes the beginning of the next line
            new_lines.append(current_line)
            current_line = current[j] 
            current_width = len(current[j])
            if j != len(lines[i])-1:#only adds a space after the word if it is not the last word of the entire line.
                current_line += " " 
                current_width += 1
                
new_lines.append(current_line)

        
out_file = open(out_file_name,"w")
for line in new_lines:
    if line == "\n":#if the line happens to be a new line charcter on it's own, it is printed with end="" to prevent a double new line occurence
        print(line,file=out_file,end="")
    else:
        print (line,file=out_file)
out_file.close()



