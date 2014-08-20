#Chantel Foot
#Assignment 9
#Question 2


inputfile = input("Enter the input filename:\n") #get name of the input file 

outputfile= input("Enter the output filename:\n") #get name of the output file

linewidth = input("Enter the line width:\n") #enter the width of the line
linewidth = int(linewidth) #convert line width into an integer

linewidth =  linewidth + 1 #add 1 to the given line width inputted (line 5)


writefile = open(outputfile, "w") #write to the file. "w" means write
infile = open(inputfile, "r") #open to read file
readlines = infile.read() #read all of the file


def main(string,length): 
    
    the_string = string[:length] #from postion 0 to the value of the length of the string
    stringlength = len(string) #stringlength is the length of the string
    if stringlength > length: #if length of string is greater than length in the function then, 
        
        if(string[:length + 1] == " "): # if equals space then, 
            writefile.write(the_string + "\n") #write to the file 
            main(string[length:],length) #run the new two values through the main function. 
       
            
        else: #if condition above not met then do the following, 
            last_char = the_string[::-1]  
            blankspace = last_char.find(" ") #find the spaces in last_char 
            line = last_char[blankspace:] #from blankspace to end
            end = last_char[:blankspace] #beginning to blank space
             
             
            writefile.write(line[::-1] + "\n") #write to the file
            main(end[::-1] + string[length:],length) #run these values through the main function. 
            
    else:
        writefile.write(string + "\n\n") 
        
        

if "\n\n" in readlines:
    readlines = readlines.replace("\n", " ") #replace the \n with a blankspace. 
    paragraph = readlines.split("  ") #split where there is a blankspace. 
    for i in paragraph:
        main(i,linewidth) #run these variables through the main function 

        
else:
    readlines = readlines.replace("\n"," ") #replace as above
    main(readlines,linewidth) #run these varibles through the main function
    
    
infile.close() 
writefile.close() #close both files so content can be saved. 