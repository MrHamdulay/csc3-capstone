#Ryan Nobin
#NBNRYA001
#Assignment 9
#15/05/14
#Question 2

inputFile = input("Enter the input filename:\n") 

f = open (inputFile,"r")
lines=f.read() 
f.close ()

outputFile = input("Enter the output filename:\n") 
width = eval(input("Enter the line width:\n")) 

lines = lines.replace("  "," $ ")
lines = lines.replace("\n"," ")
f = open(outputFile,"w")

words = lines.split(" ") 

wiz = 0

if "$" in words:
    ind = words.index("$")
    words[ind] = "  "

for i in range(0,len(words)): 

    if words[i]=="  ":
        print(" ",end="",file=f)
    elif words[i]=='':
        print("\n",file=f)
        wiz=0
        
    elif(words[i]!=" "):
        
        if wiz+len(words[i])<=width:
            print(words[i]," ",sep="",end="",file=f)
            wiz+=len(words[i])+1
        else:
            print("\n",words[i]," ",sep="",end="",file=f)
            wiz = len(words[i])+1
        
f.close()
