#Done By Guy Green 
#Question 2 Assignment 9 
#Formatting a file

#Asking for input
GivenFile=input("Enter the input filename:\n")
ProducedFile=input("Enter the output filename:\n")
LengthWanted=eval(input("Enter the line width:\n"))

#Working with Files
f=open(GivenFile, "r")
lines=f.readlines()
f.close()

Words=[]
for i in range(len(lines)):
    lines[i]=lines[i][:-1] #Taking away "\n" from the last character of each item in the list

for j in range(len(lines)):
    if lines[j]=="":
        Words.append("\n") # If there is a new paragraph
    else:
        Words.append(lines[j].split(" ")) #Creating a list where each item is a word

#Creating/Overwriting the new file
f=open(ProducedFile, "w")
CharacterNumber=0

for k in range(len(Words)):
    for l in range(len(Words[k])):
        if Words[k][l]=="\n": #To Create a new paragraph
            CharacterNumber=0
            print("\n", file=f)
            continue
        elif len(Words[k][l])+CharacterNumber>LengthWanted: #If the word won't fit on the line
            print("\n"+Words[k][l], end=" ", file=f)
            CharacterNumber=len(Words[k][l])+1
        elif len(Words[k][l])+CharacterNumber<=LengthWanted: #If the word does fit on the line
            CharacterNumber+=len(Words[k][l])+1
            print(Words[k][l], end=" ",file=f)
        
            
f.close() #Finished with File