"""Assignment 9 
Question 2
Itumeleng Nqoko
Thursday 15th May 2014"""
infile=input("Enter the input filename:\n")
outfile=input("Enter the output filename:\n")
width=input("Enter the line width:\n")

f=open(infile,"r")
lines=f.readlines()
templis=[]

for i in lines:
    templis=lines.replace(" \n"," ")
    
print(templis)


    
        
    
    