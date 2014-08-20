"""program to forma lines to a given length
yasha longstaff
15 May 2014"""

import textwrap 

def  format():
    input_file = input("Enter the input filename:\n") #get input file from user
    output_file = input("Enter the output filename:\n") #get output file from user
    required_width = eval(input("Enter the line width:\n")) #get desired length to format file
    
    
    f = open (input_file, "r") # open given file
    line = f.read() 
    if line.count("\n\n") > 0: # if input file contains paragraphs
        paragraphs = line.split("\n\n") # change text to seperate strings             
    f.close() # close the input file
    
    if line.count("\n\n") > 0: # for a file that contains paragraphs
        line = []
        for x in paragraphs: 
            sentence = textwrap.wrap(x,required_width) 
            line += sentence
            line += " " # add a space between paragraphs
    else: # for a file that contains no paragraphs
        line = textwrap.wrap(line,required_width)
    
    g = open(output_file, "w")  #access output file and wipe all existing information
    for i in line: 
        print(i, file = g)
    g.close() # close the output file
    
format()