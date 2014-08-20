"""Shriya Roy
16 May 2014
program to reformat a file"""
import textwrap
def mainp():
        filename=input("Enter the input filename:\n")
        output=input("Enter the output filename:\n")
        width=eval(input("Enter the line width: \n"))
        file_=open(filename, "r")  
        temporary=file_.read()
        newline=temporary.split("\n\n")
        file_.close()
        
        file_1=open(output,"w")
        
        for i in newline:
                i=i.replace("\n"," ")
                i=textwrap.wrap(i,width)
                
                for j in range(len(i)):
                        print( i[j],file=file_1)
                print(file=file_1)
        file_1.close()
        
mainp()

