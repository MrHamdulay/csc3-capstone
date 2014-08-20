"""File line length modifier
Christoher Sterley
11/05/2014"""

import string #in order to use the punctuation function

file_open=input("Enter the input file name:\n") #get the required file name from user

f=open(file_open,"r") #open file that user requires
file_manager=f.read() #assign file to another variable so that the information can be used even when the file is closed
f.close() #close file for efficiency

if "\n" in file_manager: #check for and remove the lines spaces
    file_manager=file_manager.replace("\n\n","%%%")
    file_manager=file_manager.replace("\n"," ")
    file_manager=file_manager.replace("%%%"," \n\n")

file_output=input("Enter the output file name:\n") #get the output file name

line_width=eval(input("Enter the line width:\n")) #get the desired line width

count=0

create=open(file_output,"w") #empty file just in case there is a lingering file
print("",file=create)
create.close()

while file_manager:
    count+=1
    if len(file_manager)>count and file_manager[count]=="\n":
        output=open(file_output,"a")
        output.write(file_manager[:count])
        output.close()
        
        file_manager=file_manager[count:]
        count=0
        
    elif count==line_width and len(file_manager)>count:
        while file_manager[count].isalpha() and count!=0 or file_manager[count] in string.punctuation: #check through word until a non-alphabetic character is found, or the start of the word is reached
            count-=1
        if count==39 and file_manager[count]==" " and file_manager[count+2]==" ":#punctuation or single letter word
            output=open(file_output,"a")
            output.write(file_manager[:count+2]) #write to the ouput file
            output.write("\n")
            output.close()
            
            file_manager=file_manager[count+3:]#gets rid of the space as well as all the preappended string
        else:
            output=open(file_output,"a")
            output.write(file_manager[:count]) #write to the ouput file
            output.write("\n")
            output.close()
            if file_manager[count]==" ": #check ensures letters dont get cut off
                file_manager=file_manager[count+1:] #remove part of string which has already been added to file
            else:
                file_manager=file_manager[count:]
        count=0
    elif len(file_manager)<count and count==line_width: #adds final part of string to the end of the file
        output=open(file_output,"a")
        output.write(file_manager) #write to the ouput file
        output.close()
        break    