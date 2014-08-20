"""Assignment 9 Question 2 

Reformat text according to a specific collumn width
Shaheen Karodia
KRDSHA003"""

import textwrap
#get inputs from the user
x=input("Enter the input filename:\n")
y=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))



#get all the information from one file 
f=open(x, "r")
lines=f.readlines() #get all lines into one variable
f.close()

#open a new file to write to
outfile=open(y, "w")


final_text=""


for line in range(len(lines)):    #interate through each line
    if lines[line]=="\n":         #check to see  if its the end of a paragraph
        
    
        final_text=textwrap.wrap(final_text, width)   #wrap the current paragraph
        
        for i in range (len(final_text)):
            print(final_text[i], file=outfile)    #prints a paragraph to the new file
        print("", file=outfile)                   #ensures there is a space between paragraphs
        
        final_text=""              #reinitialises the text for the next pragraph
        
    elif line==len(lines)-1:  #checks to see if it is the last line 
        
        final_text=final_text+lines[line]
        final_text=textwrap.wrap(final_text, width)
        
        for i in range (len(final_text)):
            print(final_text[i], file=outfile)    #prints a paragraph to the new file
            
       
    else:  
        final_text=final_text+lines[line]
        
                

        
outfile.close()        
        
        
        
        
  
                    
                    
            
            
            
        
    
        


