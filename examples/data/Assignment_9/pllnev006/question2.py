# Reading in from a file and outputting a formated version to another file
# Nevarr Pillay - PLLNEV006
# 12 May 2014


def readin(filename):
    """Reads an entire file into one string and returns it"""
    file = open(filename,"r") # File to read from with given file name
    strings = file.read()
    file.close()    
    return strings

def prepareString(string):
    """Reads in a string an removes all new line characters unless its a new paragraph"""
    newstring = ""
    count = 0
    while count < (len(string) - 1): # Removes all new line characters unless there are two for a paragraph in which case one is left
        if string[count] == "\n" and string[count + 1] != "\n":
            newstring += " "
            count += 1
        elif string[count] == "\n" and string[count + 1] == "\n":
            newstring += string[count]
            count += 2            
        else:
            newstring += string[count]
            count += 1
            
    return newstring        
    
def formatFile(strings,width):
    """Format the string into lines with given width"""
    newstring = "" # A new string that is going to be returned
    while True:
        if len(strings)<(width): # If the length of the string is less than the width, the string is added to the end of newstring and the loop is ended
            newstring += strings
            break
        else: # If the length of the string is longer than the width
            templine = strings[:width] # A temporary line which is a substring from the beginning of the string until index of width
            if templine.count("\n") > 0: # If a newline chracter is found in the line indicating a new paragraph
                index = templine.find("\n")
                newstring += templine[:index+1] + "\n" # Substring of templine from beginning to index of \n is added plus another \n 
                strings = strings[index+1:] # String is set to one after index of \n
            else:    
                if templine[-1] == " ": # If the character at the end of the line is a space                      
                    newstring += templine + "\n" # Add the temporary line to the newstring and add a newline character to the end 
                    strings = strings[width:] # Make strings the substring of strings beginning at one character after index of width 
                elif strings[width] == " ": # If the character after the end of the line is a space
                    newstring += templine + "\n" # Add the temporary line to the newstring and add a newline character to the end 
                    strings = strings[width +1:] # Make strings the substring of strings beginning at index of width                 
                else: # If end of temporary line is middle of a word
                    num = width-1
                    while templine[num] != " ": # Find the index of the space just before the word
                        num -= 1
                    newstring += templine[:num+1] + "\n" # Add the substring of the temporary line up until the index of the space to the newstring and add a newline character to the end 
                    strings = strings[num+1:] # Make strings the substring of strings beginning at one character after index of space
    return newstring         

def output(filename,out):
    """Writes the given string to a file"""
    f = open(filename,"w") # File to write to with given file name
    print(out,file=f,end="")
    f.close()       
    
def main():
    inFile = input("Enter the input filename:\n")
    outFile = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    newinfo = formatFile(prepareString(readin(inFile)),width)    
    output(outFile,newinfo)

if __name__ == "__main__":
    main()

