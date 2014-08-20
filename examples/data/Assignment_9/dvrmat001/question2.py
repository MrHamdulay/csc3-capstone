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

chars = 0

if "$" in words:
    ind = words.index("$")
    words[ind] = "  "

for i in range(0,len(words)): 
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