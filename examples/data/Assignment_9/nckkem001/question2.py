"""Program to format length of lines in a supplied text file and write the formatted text to a new file.
Kemeshan Naicker
15 May 2014"""

def format_text():
    
    #Prompt user for location of input file.
    inputfile = open(input("Enter the input filename:\n"), "r")
    #Read data from input file into a list of lines.
    string = inputfile.readlines()
    inputfile.close()
     
    #Prompt user to name the output file.
    outputfile = open(input("Enter the output filename:\n"), "w")
    
    #Clean up the list of strings by deleting leading spaces and newline characters
    #at the end of every line of text (Not newline characters that serve to introduce
    #a new paragraph.)
    for i in range(len(string)):
        if string[i][0] == " ":
            string[i] = string[i][1:]
        if string[i][-1:] == "\n" and string[i] != "\n":
            string[i] = string[i][:-1]
    
    #Separate the string into a list of individual words (remaining newline characters
    #are treated as individual items in the list.)
    string = " ".join(string)
    wordlist = string.split(" ")
    
    #Prompt user for the formatted line width.
    linewidth = eval(input("Enter the line width:\n"))
    
    #Counter variable prints lines when the addition of a new word would cause the line
    #width to exceed the desired formatted width.
    counter = 0
    line = ""
    
    for i in range(len(wordlist)):
        
        if wordlist[i] == "\n": #Print lines (regardless of length) if they are
            #terminated by a newline character.
            print(line,"\n", file = outputfile)
            #Reset the current line and counter.
            line = ""
            counter = 0
        
        #Add words to a line if doing so will not result in the line exceeding the
        #desired width.
        elif counter + len(wordlist[i]) <= linewidth:
            counter += len(wordlist[i])
            line += wordlist[i]
            if counter < linewidth:
                counter += 1
                line += " "
        
        #If adding a word causes a line to exceed the desired width, print the old line
        #and use the word to start a new line, re-initiatilising the counter.
        else:
            print(line, file = outputfile)
            counter = len(wordlist[i])+1
            line = wordlist[i]+" "
    
    #Print any remaining text (with length obviously in compliance with the specified
    #format.
    if line:
        print(line, file = outputfile)
        
    outputfile.close()
    
if __name__=="__main__":
    format_text()