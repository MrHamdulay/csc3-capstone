"""Assignment 9 Question 2
Muzammil Jable
14 May 2014"""

infileName=input("Enter the input filename:\n") #obtain input file from user          
infile=open(infileName,"r")  #open the specified file in read mode                        
contents=[]                                             
for line in infile: #iterate through each line in the file                                      
    contents.append(line)                               
infile.close()   #close file

new_file=input("Enter the output filename:\n")# obtain input from user for output file name
width=eval(input("Enter the line width:\n")) # obtain input from user for line width

for line in range(len(contents)):  #iterate through list 
    if contents[line]=="\n":  #remove return carriage
        pass
    elif contents[line][-1:]=="\n":  #check for end of old line
        contents[line]=contents[line][:-1]   # remover return carriage
content=[]      # create empty list 
for line in range(len(contents)):  #loop through list of lines
    contents[line]=contents[line].split(" ") #split each line into a list of words
    for word in range(len(contents[line])):  # iterate over word in each line
        content.append(contents[line][word])            

output_file=open(new_file,"w")    #open specified output file in writing mode
line=""  # create line variable
while True:
    try:
        if content[0]=="\n":  #see if line is empty
            line=line+content[0]   
            print(line,file=output_file)  #add the line to the file
            content.remove(content[0])  #remove the new line character from the list of words
            line="" #re-create the line variable
        elif line=="":  #check for beginning of line
            line=content[0] #add word to line
            content.remove(content[0]) 
        elif len(line+" "+content[0])<=width:           
            line=line+" "+content[0]                    
            content.remove(content[0])                  
        else:
            print(line,file=output_file)                
            line=""    
    except:  #if error appears 
        print(line,file=output_file) # add the remaining line to file
        output_file.close()#close file
        break #stop the indefinite loop