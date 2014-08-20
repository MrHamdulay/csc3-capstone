"""assignment 9 question 2
shannon clacey
13 may 2014"""

input_file = input("Enter the input filename:\n") #gets the files to be used as input from the user
output_file = input("Enter the output filename:\n")

linewidth = input("Enter the line width:\n") #establishes the line width to be used
linewidth = eval(linewidth) +1 #adjusts the length by adding on one

def reformat(string,length): #create function with parameter string and length
    user_string = string[:length] #formats the string to go only until the length required through slicing
    stringlength = len(string) 
    
    if stringlength > length: #determines whether the string is longer than it ought to be or not
        
        if(string[:length + 1] == " "): #seeing if the string is empty
            writefile.write(user_string + "\n")
            reformat(string[length:],length)
            
        else:
            lastchar = user_string[::-1]
            whitespace = lastchar.find(" ")
            eoline = lastchar[whitespace:]
            uptoend = lastchar[:whitespace]
            
            writefile.write(eoline[::-1] + "\n")
            
            reformat(uptoend[::-1] + string[length:],length)
    else:
        writefile.write(string + "\n\n") #adjustments not necessary if the string is not too long i.e. not longer than specified length
        
writefile = open(output_file, "w") #open the output file which will be overwritten
infile = open(input_file, "r") #open the input file which will be read
readline = infile.read() #read the file into one long string 

if "\n\n" in readline:
    readline = readline.replace("\n", " ")
    paragraph = readline.split("  ")
    for loop in paragraph:
        reformat(loop,linewidth)
        
else:
    readline = readline.replace("\n"," ")
    reformat(readline,linewidth) 
    
infile.close() #close the files used
writefile.close()
