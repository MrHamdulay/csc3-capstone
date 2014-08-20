#Ariel Rubin
#RBNARI001
#porgram that reformats a textfile so all the lines are at a given length
#13 May 2014

amount = 0
check = 0

#reformat function to check to see if the line is the correct size and if line isn't it moves part of line down to the next line
def reFormat(line,width,temp): 
    
    global amount
    global check
    
 #If there is a blank line the program adds another \n character in order to keep the paragraphs    
    if(line == "\n"): 
        amount = 0
        return(line + "\n")
    
    elif((len(line) <= int(width))): 
        
        check = amount + len(line)
        
        if(check > int(width)):
            pos = line.rfind(" ",0,(int(width)-amount+1)) 
            amount = 0
            check = 0
            temp = line[:(pos+1)] + "\n"
            return(temp + (reFormat(line[(pos+1):],width,temp)))
       
        #This amount represents the number of characters on a line, if another string is put next to this it takes into account that there is already this number of chars in the line       
        else: 
            amount = len(line)  
         
#checks to see if the 2nd last character of the line isnt a space, if 2nd line is a space program does nothing and if there isnt it a space then the program adds a space           
            if(line[amount-2]!= " "): 
                line = line[:amount-1] + " " 
            else:
                line = line[:amount-1] 
            
 #returns newly formatted line            
            return (line) 
   
 #If none of the above conditions are met the program works out the position of the last space before the 40 char limit is met, and then adds the correct lines    
    else:
       
        pos = line.rfind(" ",0,(int(width)-amount+1)) 
        amount = 0 
        check = 0
        temp = line[:(pos+1)] + "\n"
        
#rechecks left over part and adds it to the correct part        
        return(temp + (reFormat(line[(pos+1):],width,temp))) 
           
#main method
def main(): 
   
    global amount
    
    paragraph = ""
    width = 0
    amount = 0
    
#asks the user to input values
    
    print("Enter the input filename:")
    File_name = input()
    print("Enter the output filename:")
    Out_File_name = input()
    print("Enter the line width:")
    width = input()
    
#opens file and reads it into an array
    
    f = open (File_name, "r")
    text = f.readlines()
    f.close()
    
#opens file again and creates a loop which iterates through each line of the array, and then creates a total string called paragraph which stores the final version of the formated file which will be written to the file
    
    f = open (Out_File_name, "w")
    for i in range(len(text)):
        temp = ""
        paragraph = paragraph + (reFormat(text[i],width,temp))
#writes the paragraph to the file    
    f.write(paragraph) 
    f.close()

main()    