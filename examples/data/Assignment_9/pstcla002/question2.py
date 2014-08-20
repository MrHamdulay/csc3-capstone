"""program to format a text file to make lines same given length
Claudia Pastellides
12 May 2013"""
input1 = input("Enter the input filename:\n")
output1 = input("Enter the output filename:\n")
linewidth = input("Enter the line width:\n")
linewidth = int(linewidth)
linewidth += 1

def main(string,length): #main program slices string into line width
    mystring = string[:length]
    stringlength = len(string)
    if stringlength > length:
        
        if(string[:length + 1] == " "): 
            writefile.write(mystring + "\n") #adding \n to mystring in file
            main(string[length:],length) #rerun main from begginging half of string and length given
        else:
            lastchar = mystring[::-1]
            whitespace = lastchar.find(" ") #searches for space
            eoline = lastchar[whitespace:]  #splits reversed string from space to end
            uptoend = lastchar[:whitespace] #splits reveresed string from beggining to space
            
            writefile.write(eoline[::-1] + "\n")
            main(uptoend[::-1] + string[length:],length)
    else:
        writefile.write(string + "\n\n")
        
writefile = open(output1, "w") #open output1 to over write
infile = open(input1, "r") #open input1 to read
readline = infile.read()# read whole input file as a string

if "\n\n" in readline:
    readline = readline.replace("\n", " ") #changes space syntax to a space
    paragraph = readline.split("  ") #splits it into lines
    for loop in paragraph:
        main(loop,linewidth)
        
else:
    readline = readline.replace("\n"," ")
    main(readline,linewidth)
    
infile.close()
writefile.close()