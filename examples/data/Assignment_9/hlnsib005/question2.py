"""Sibulele Hlongwane
Date: 14 May 2014
Assignment 9: Reformat a text file"""
import math 

amount=0
suml=0
filename= input("Enter the input filename:\n")
f= open(filename,"r")
lines=f.readlines()
outfile= input("Enter the output filename:\n")
fo = open (outfile, "w")
width= eval(input("Enter the line width:\n"))

    
for j in range (len (lines)):
    if len(lines[j])>width-1:
        lines[j] = lines[j][:-1]
    if lines[j]=="":
        sline=lines[j]
    else:
        sline= lines[j].split(" ")

        
    if len(lines[j])<=width-1:
        for i in range(len(sline)):
            print(sline[i],file=fo,end=" ")
       
    else:
        length=(len(lines[j]))
        maxlength=(width-1)   
       
        for i in range(len(sline)):
          
            if (suml+len(sline[i]))<(width-1):
                suml=suml+len(sline[i])+1
                print(sline[i],file=fo, end=" ")
            else:
                if sline[i]==" ":
                    print("\n", file=fo)
                    suml=len(sline[i])
                else:
                    print("\n"+sline[i],file=fo,end=" ")
                    suml=len(sline[i])
                

            
fo.close()
f.close()

