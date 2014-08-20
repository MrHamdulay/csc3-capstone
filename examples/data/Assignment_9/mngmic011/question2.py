"""Question 2 - Create paragraph of formatted to specific width
Assignment 9
Micaela Menegaldo
14 May 2014"""

import textwrap

if __name__=='__main__':
    inputfile=input("Enter the input filename:\n")
    outputfile=input("Enter the output filename:\n")
    lwidth=input("Enter the line width:\n")
    
    f=open(inputfile,"r")
    entirefile=f.read()
    f.close()   
    
    lines=entirefile.split("\n\n")
    
    newfile=[]
    for i in range(len(lines)):
        paragraph=textwrap.wrap(lines[i],width=eval(lwidth))
        newfile.append(paragraph)
    
    for i in range(len(newfile)):
        newfile[i].append(" ")

    f=open(outputfile,"w")
    for para in range(len(newfile)):
        for line in range(len(newfile[para])):
            print(newfile[para][line],file=f)
    f.close()
    