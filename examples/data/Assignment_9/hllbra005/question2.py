# Program to reformat a text file so that all lines are at most a given length
# Brandon Hall
# 16/05/2014

amount = 0
check = 0

def reFormat(line,width,temp): # This is the reformat method and checks to see if the line is the correct size and if it isn't it moves part of it down to the next lien
    
    global amount
    global check
    
    if(line == "\n"):  # If there is a blank line it adds another \n char in order to keep the paragraphs
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
       
        else: 
            amount = len(line)  # This amount represents the amount of characters on the line, if another string is put next to this it takes into account that there is already
                            # this number of chars on the line
         
            if(line[amount-2]!= " "): # This checks to see if the second last character of the line isnt a space, if it is it does nothing and if it isnt it adds a space
                line = line[:amount-1] + " " 
            else:
                line = line[:amount-1] 
            
            return (line)  # This returns the newly formatted line
   
    else: # If none of the above conditions are met it works out the position of the last space before the 40 char limit is met, and then adds the correct lines
       
        pos = line.rfind(" ",0,(int(width)-amount+1)) 
        amount = 0 
        check = 0
        temp = line[:(pos+1)] + "\n"
        
        return(temp + (reFormat(line[(pos+1):],width,temp))) # This rechecks the part left over and adds it to the correct part
           
def main():    # Main method
   
    global amount
    
    paragraph = ""
    width = 0
    amount = 0
    
    # The below is the messages to the user
    
    print("Enter the input filename:")
    File_name = input()
    print("Enter the output filename:")
    Out_File_name = input()
    print("Enter the line width:")
    width = input()
    
    # Below opens the file and reads it into an array
    
    f = open (File_name, "r")
    text = f.readlines()
    f.close()
    
    # opens the file again and then creates a loop which iterates through each line of the array, it then creates a total string called paragraph which
    # stores the final version of the formated file which will be written to the file
    
    f = open (Out_File_name, "w")
    for i in range(len(text)):
        temp = ""
        paragraph = paragraph + (reFormat(text[i],width,temp))
    f.write(paragraph) # This writes the paragraph to the file
    f.close()

main()    