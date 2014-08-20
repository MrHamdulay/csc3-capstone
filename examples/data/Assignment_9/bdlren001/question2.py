# a program to reformat a text file so that all lines are at most a given length
# BDLREN001
# Budeli Rendani
# 14/05/2014

import textwrap # importing textwrap for merging the file withi the given width
def main():
    infilename=input("Enter the input filename:\n") # obtaining the file file to copy from
    outfilename=input("Enter the output filename:\n") # Obtaining the file to overwrite
    width=eval(input("Enter the line width:\n")) # obataing the width from the user

    infile=open(infilename, "r") # opening the file for reading
    outfile=open(outfilename, "w") # opening the file for overwriting
    
    # placing the words in an empty sting as one long string
    s=""
    for i in infile:
        s+=i
    # wrapping up the string within the given width
    print(textwrap.fill(s,width), file=outfile)
    infile.close()# closing the file where the data was extracted
    outfile.close() # closing the file which was overwritten 
main()