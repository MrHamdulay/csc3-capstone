# Yudhi Moodley
# Assignment 9- question 2
# 16/05/2014


import textwrap

infile_name=input("Enter the input filename:\n")
outfile_name=input("Enter the output filename:\n")
w=eval(input("Enter the line width:\n"))

infile= open(infile_name, "r")
#make the contents of the file into a list
lines=infile.readlines()  
infile.close()

outfile= open(outfile_name, "w")
#creates a string
words=""                       

for i in range(len(lines)):
    #paragraph ends, print words, format to file)
    if lines[i]=="\n":         
        paragraph=textwrap.wrap(words, width=w)
        
        for j in range(len(paragraph)):
            
            if j==len(paragraph)-1:
                #end of the paragraph, print new line before next 
                print(paragraph[j], "\n", file=outfile) 
            else:
                print(paragraph[j], file=outfile)
        #empty the string forms new paragraph
        words=""                
        
    else:
        #lines in the string
        words+=lines[i]  
        
#last paragraph        
final=textwrap.wrap(words, width=w)  
for k in final:
    print(k, file=outfile)
        
    
outfile.close()





