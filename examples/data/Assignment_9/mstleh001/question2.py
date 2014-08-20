""" a program to fix the length of each line of paragraphs
Lehlogonolo Masetla
13 May 2014"""

file_name=input("Enter the input filename:\n")    # prompt filename from user

file=open(file_name,"r")                       
contents=[] 

for line in file:                                 # loop through every line                            
    contents.append(line)                               
file.close()                                      # close file

file1=input("Enter the output filename:\n")       # prompt for the output file
width=eval(input("Enter the line width:\n"))      # prompt for width

for line in range(len(contents)):
    
    if contents[line]=="\n":
        pass
    elif contents[line][-1:]=="\n":               # check for end of old line
        contents[line]=contents[line][:-1]        
        
contents2=[]                                      # assign an empty array
for line in range(len(contents)):
    contents[line]=contents[line].split(" ")      # assign each line to a string
    for word in range(len(contents[line])):
        contents2.append(contents[line][word])            

output_file=open(file1,"w")                       # open to write in output file
line=""                                           # for paragraphing

while True:
    try:
        if contents2[0]=="\n":                    # check the content of list
            line=line+contents2[0]   
            print(line,file=output_file)          # add the line to the file
            contents2.remove(content[0])            # remove the new line character from the list of words
            line=""                               # re-create the line variable
            
        elif line=="":                            # check for beginning of line
            line=contents2[0]                     # add word to line
            contents2.remove(contents2[0]) 
            
        elif len(line+" "+contents2[0])<=width:           
            line=line+" "+contents2[0]                    
            contents2.remove(contents2[0])                  
        else:
            print(line,file=output_file)                
            line=""  
            
    except:                                       # error handling
        print(line,file=output_file) 
        output_file.close()
        break                                     # break the loop