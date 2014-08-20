# Aaron Krishna
# 15 May 2014
# A program to reformat a text file so that all lines are at most a given length

input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
length = int(input("Enter the line width:\n"))
line = 0

f = open(input_file, "r") # ---reading section---
lines = f.readlines() 
f.close()

for i in range (len(lines) - 1): 
    lines[i] = lines[i][:-1] #removes nextline character

word_array = [] 

for i in range(len(lines)): 
    if lines[i] != "": 
        word_array.append(lines[i].split(" ")) #split into seperate words
    else: 
        word_array.append(["\n\n"]) #check for paragraph
        
f = open(output_file, "w") # ---overwriting section---
for i in range(len(word_array)): 
    for j in range(len(word_array[i])): 
        if line == 0: 
            line = len(word_array[i][j]) + 1
            print(word_array[i][j], end = " ", file = f) #paragraph's first word 
        elif word_array[i][j] == "\n\n": 
            line=0
            print(word_array[i][j], sep = "", end = "", file = f) #paragraph blank line
        elif len(word_array[i][j]) + line > length: #wrap wrap wrap it 
            print("\n" , word_array[i][j], sep = "", end = " ", file = f) 
            line=len(word_array[i][j]) + 1
        else: 
            if len(word_array[i][j]) + line <= length:
                line += len(word_array[i][j]) + 1 #just in case 
                print(word_array[i][j], end = " ", file = f) 
            else: 
                print(word_array[i][j], end = "", file = f) 
f.close() 