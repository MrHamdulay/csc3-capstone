""" program to format a text file
Litha Maqungo
Assignment 9"""
#starting off with the opening prompts to get all the data needed
openinginput= input("Enter the input filename: \n")
closingoutput=input("Enter the output filename: \n")
wanted_width= eval(input("Enter the line width: \n"))
wanted_width += 1

def main(input_string, length): #creating the main body of the program
    new_string = input_string[ :length] #slicing the string
    input_length = len(input_string) #finding the length of the string input
    if input_length > length: #main if statement depends on if the length of the inputted string is longer than the length desired
        if input_string[ :length + 1] == " ": 
            editfile.write(new_string + "\n") #\n added in the file
            main(input_string[length: ],length) #goes back and does main again from the first half of input_string and length 
        else:
            endcharacter = input_string[::-1]
            whitespace = endcharacter.find(" ") #looks for spaces without characters
            endofline = endcharacter[whitespace:] #split works from the whitespace to the end
            startend = endcharacter[:whitespace] #split works from the beginningn until the whitespace
            
            editfile.write(endofline[::-1] + "\n") #adding in \n
            main(startend[::-1] + input_string[length:], length)
    else:
        editfile.write(input_string + "\n\n")
#information which feeds into the body of the program       
editfile=open(closingoutput, "w") #allows for the file to be overwritten
readfile= open(openinginput, "r") #allows for the file to be read
readline= readfile.read() #looks at the input file as a string
if "\n\n" in readline:
    readline = readline.replace("\n", " ") #converts the representation for a space into an actual space
    body = readline.split("  ") 
    for a in body:
        main(a, wanted_width)
else:
    readline=readline.replace("\n", " ")
    main(readline, wanted_width)
readfile.close()
editfile.close()