"""Assignement 9, Question 1
Tejasvin Bagirathi
Program to format lines of text to specific width"""
    
#User enters input and output file
inFile = open(input("Enter the input filename:\n"), "r")
#Data from inFile is read into lines variable
lines = inFile.readlines()
inFile.close()
     
#User enters output file
outFile = open(input("Enter the output filename:\n"), "w")
    
#Delete spaces and \n characters in lines
#at the end of every line (exclude \n characters that lead to a new paragraph)
for i in range(len(lines)):
    if lines[i][0] == "":
        lines[i] = lines[i][1:]
    if lines[i][-1:] == "\n" and lines[i] != "\n":
        lines[i] = lines[i][:-1]
    
#String separated into list of words (\n characters are separate items in list)
lines = " ".join(lines)
words = lines.split(" ")
    
#User enters desired line width
line_width = eval(input("Enter the line width:\n"))
    
#Count variable to prevent lines that would exceed the width from beign printed
count = 0
new_line = ""
    
for i in range(len(words)):
    if words[i] == "\n": #Print line if they end with \n
        print(new_line,"\n", file = outFile)
        #Reset new line and count to 0
        new_line = ""
        count = 0
        
    #Add words to a new line as long as it not greater than line_width
    elif count + len(words[i]) <= line_width:
        count += len(words[i])
        new_line += words[i]
        if count < line_width:
            count += 1
            new_line += " "
        
    #If adding a word causes a line width to be larger than the width, then print the old line
    #The end word is used to start a new line. Also reset count
    else:
        print(new_line, file = outFile)
        count = len(words[i])+1
        new_line = words[i]+" "
    
#Print any remaining text, provided it is not bigger than the line width
if new_line:
    print(new_line, file = outFile)
#Close output file  
outFile.close()
