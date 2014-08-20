#Assignment 9, Question 2
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Modified: 16/05/2014

#This function grabs a text and converts it to desired length per line.
def conciseText(text, size):
    lines = []
    while len(text) > size: #Checks length of text with character limit
        index = text[:size].rfind(" ") #Finds the first space within character limit so as word is not stripped.
        lines.append(text[:index]) #Appends text to lines[]
        text = text[index+1:]
    lines.append(text)
    return( "\n".join(lines)) #Return Output


#Checking if program is being run as standalone.
if __name__ == '__main__':
    
    file = input("Enter the input filename:\n") 
    
    #Opening file.
    f = open(file, "r")
    myText = f.read()
    f.close()
    
    output = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))  
    #Printing out every line, taking care of paragraphs.
    f = open(output, "w")
    
    text = []
    
    for paragraph in myText.split("\n\n"):
        text.append(paragraph.replace("\n", " "))
     
    for paragraph in text:
        print(conciseText(paragraph,width),file=f)        
        print(file=f)
    
    f.close()