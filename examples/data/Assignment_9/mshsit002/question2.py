"""a program to reformat a text file so that all lines are at most a given length.
sithembiso Mashinini
16 May 2014"""

from textwrap import *

def text_edit(input_file, output_file, width):
    infile = open(input_file,"r")
    outfile = open(output_file, "w")
    lines = infile.read()
    content = lines.split("\n\n")
    
    for item in content:
        item_1 = item.replace("\n"," ")    
        Newst = wrap(item_1,width)   
        
        for string in Newst:                     
            print(string, file = outfile)           
        print(file = outfile)
        
     
    outfile.close()
    infile.close()
        
if __name__ == '__main__':
    
    input_file = input("Enter the input filename:\n")
    output_file = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n")) 
    
    text_edit(input_file, output_file, width)