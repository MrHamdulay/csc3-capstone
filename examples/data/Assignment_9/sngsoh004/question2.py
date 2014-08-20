#Soham Singh
#SNGSOH004
#Assignment 9
#Question 2

inputFile = input("Enter the input filename:\n") #Asking for the name of the input file

f = open (inputFile,"r")

lines=f.read() #Storing the content of the input file into a single string

f.close ()

outputFile = input("Enter the output filename:\n") #Asking for the name of the output file to be created


width = eval(input("Enter the line width:\n")) #Asking for the width in characters of the printout

lines = lines.replace("  "," $ ")
lines = lines.replace("\n"," ")
f = open(outputFile,"w")

words = lines.split(" ") #splitting the contents of the original file by a space character

chars = 0

if "$" in words:
    ind = words.index("$")
    words[ind] = "  "

for i in range(0,len(words)): #For loop responsible for the printing to the output file
    if words[i]=="  ":
        print(" ",end="",file=f)
    elif words[i]=='':
        print("\n",file=f)
        chars=0
        
    elif(words[i]!=" "):
        
        if chars+len(words[i])<=width:
            
            print(words[i]," ",sep="",end="",file=f)
            
            chars+=len(words[i])+1
            
        else:
            
            print("\n",words[i]," ",sep="",end="",file=f)
            
            chars = len(words[i])+1
        
f.close()