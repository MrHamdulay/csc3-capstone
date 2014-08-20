#Asil Motala
#MTLASI002
#Assignment 9
#Question 2
#09 May 2014

file_name=input("Enter the input filename:\n")          #get file name from user
file=open(file_name,"r")                                #open file in read mode
contents=[]                                             #initialize empty list
for line in file:                                       #loop through file
    contents.append(line)                               #add each line of file to list
file.close()                                            #close file

new_file=input("Enter the output filename:\n")          #get input from user for output file name
width=eval(input("Enter the line width:\n"))            #get input from user for line width

for line in range(len(contents)):                       #loop through list (contents of file)
    if contents[line]=="\n":                            #leave new lines (empty lines)
        pass
    elif contents[line][-1:]=="\n":                     #check for end of old line
        contents[line]=contents[line][:-1]              #remove the new line at the end of old line
content=[]                                              #intialize empty list of words
for line in range(len(contents)):                       #loop through list of lines
    contents[line]=contents[line].split(" ")            #split each line into a list of words
    for word in range(len(contents[line])):             #loop through words in each line
        content.append(contents[line][word])            #add words to a new list

output_file=open(new_file,"w")                          #open file in writing mode
line=""                                                 #intialize line variable
while True:
    try:
        if content[0]=="\n":                            #check for empty line
            line=line+content[0]                        #add new line character to the line being created
            print(line,file=output_file)                #print the line to the file
            content.remove(content[0])                  #remove the new line character from the list of words
            line=""                                     #re-intialize line variable
        elif line=="":                                  #check for beginning of line
            line=content[0]                             #add word to line
            content.remove(content[0])                  #remove word from list of words
        elif len(line+" "+content[0])<=width:           #check if adding a word and space will fit within witdth
            line=line+" "+content[0]                    #add word and space to line
            content.remove(content[0])                  #remove word from list
        else:
            print(line,file=output_file)                #check if width line is full and print full line to file
            line=""                                     #re-intialize line variable
    except:                                             #if error appears (expected error is the list index out of range, as when all words used up there is an empty list)
        print(line,file=output_file)                    #print remaining line to file
        output_file.close()                             #close file
        break                                           #break out of while loop