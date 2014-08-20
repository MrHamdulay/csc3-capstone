"""reformat a text file
Michelle Lu
11 May 2014"""

import textwrap

infile_name=input("Enter the input filename:\n")
outfile_name=input("Enter the output filename:\n")
w=eval(input("Enter the line width:\n"))

infile= open(infile_name, "r")
lines=infile.readlines()  #make the contents of the file into a list
infile.close()

outfile= open(outfile_name, "w")
words=""                       #create a string of the contents
for i in range(len(lines)):
    if lines[i]=="\n":         #when the paragraph ends, print the words with the formatting to the file)
        paragraph=textwrap.wrap(words, width=w)
        for j in range(len(paragraph)):
            if j==len(paragraph)-1: 
                print(paragraph[j], "\n", file=outfile) #when it is the end of the paragraph, print a new line before the next one
            else:
                print(paragraph[j], file=outfile)
           
        words=""                #empty the string to form the new paragraph
        
    else:
        words+=lines[i]  #add the lines into the string
        
final=textwrap.wrap(words, width=w)  #prints the last paragraph
for k in final:
    print(k, file=outfile)
        
    
outfile.close()





