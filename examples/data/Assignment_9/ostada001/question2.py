'''Adam Oosthuizen 
Text Wrap program'''
#Import print method for output in files
from __future__ import print_function
#Open files to be read and written to
rFileName = input("Enter the input filename:\n")
rF = open(rFileName,'r')
aFileName = input("Enter the output filename:\n")
aF = open(aFileName,'w')
lineWidth = eval(input("Enter the line width\n"))

#read whole file into a string
wholeString = rF.read()

def textWrap(string,integer):
    text = string.split()
    length = 0
    #loops through an array with values of the long string
    for i in range(len(text)):
        #check each line's length against the user requested length of the lines
        if length +1+len(text[i]) <= integer:
            print(text[i]+" ",end='',file =aF)
            length = length + len(text[i])+1
        #Normal case 
        elif '.'!=text[i][-1]:            
            print("\n"+text[i]+" ",end="",file =aF)
            length = len(text[i])+1
        #(Unsuccessful) check for empty line
        elif'\n'==text[i]:
            print('',file=aF)
        #full stop exception
        else:
            print("\n"+text[i]+"  ",end="",file =aF)
            length = len(text[i])+2
#call function
textWrap(wholeString,lineWidth)    
#close files
rF.close()
aF.close()