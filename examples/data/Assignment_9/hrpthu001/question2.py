"""Program to format length of lines in a supplied text file
thushar hariparsad
15 May 2014"""

def format_text():
    
    f = open(input("Enter the input filename:\n"), "r")
    #Read data from input file into a list of lines.
    string = f.readlines()
    f.close()
     
    outputfile = open(input("Enter the output filename:\n"), "w")
    
    # delete leading spaces and newline characters at the end of every line of text 
    for i in range(len(string)):
        if string[i][0] == " ":
            string[i] = string[i][1:]
        if string[i][-1:] == "\n" and string[i] != "\n":
            string[i] = string[i][:-1]
    
    #Separate the string into a list of individual words
    string = " ".join(string)
    listA = string.split(" ")
    
    line_width = eval(input("Enter the line width:\n"))
    counter = 0
    line = ""
    
    for i in range(len(listA)):
        
        if listA[i] == "\n": #Print lines if they end with newline character
            print(line,"\n", file = outputfile)
            line = ""
            counter = 0
        
        #Add words if it willnot exceed the desire width
        elif counter + len(listA[i]) <= line_width:
            counter += len(listA[i])
            line += listA[i]
            if counter < line_width:
                counter += 1
                line += " "
        
        #If adding a word causes a line to exceed the desired width, print the old line and use the word to start a new line
        else:
            print(line, file = outputfile)
            counter = len(listA[i])+1
            line = listA[i]+" "
    
    if line:
        print(line, file = outputfile)
        
    outputfile.close()
    
if __name__=="__main__":
    format_text()