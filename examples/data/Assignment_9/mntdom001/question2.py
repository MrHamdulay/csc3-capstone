"""a program to reformat a text file so that all lines are at most a given length.
Dominic Manthoko
16 May 2014"""

from textwrap import *

def text_edit(input_file, output_file, width):
    """ function that reads in a file, alters the formatting of the file and 
    saves the alterations in an output_file """
    
    # open the files
    infile = open(input_file,"r")
    outfile = open(output_file, "w")
    
    # read in the entire contents of the file as a string
    lines = infile.read()
    
    # spit the lines string(above) at '\n\n' because it represents a newline in the original file
    content = lines.split("\n\n")
    
    for item in content:
        item_1 = item.replace("\n"," ")     # remove the newline character from the string
        new_item = wrap(item_1,width)    # call the wrap function on the item 
        
        for string in new_item:                      # each item in new_item is a string which represents a line in a textfile
            print(string, file = outfile)            # print the edited lines to the outfile
        print(file = outfile)
        
    # close the files    
    outfile.close()
    infile.close()
        
if __name__ == '__main__':
    # prompt the user for input
    input_file = input("Enter the input filename:\n")
    output_file = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n")) 
    
    text_edit(input_file, output_file, width)