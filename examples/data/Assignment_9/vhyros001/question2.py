"""Assignment 9 question 2 Print file with lines a maximum length
Ross van der Heyde VHYROS001
10 May 2014"""

fName = input("Enter the input filename:\n")
#fName = "input.txt"
newName = input("Enter the output filename\n")
#newName = "output.txt"
width = eval(input("Enter the line width:\n"))

fIn = open(fName, "r")
text = fIn.readlines()
fIn.close()

for i in range(len(text)):
    if len(text[i])>1:
        text[i] = text[i].replace("\n", "")
        text [i] = text[i].split(" ")


#lines = []

length=0 #keeps track of line's length
fOut = open(newName, "w")
for j in range(len(text)):
    for i in range(len(text[j])):
        length += len(text[j][i])
        if text[j][i] == "\n":
            print("\n", file = fOut)
            length=0
        elif length >= width:        
            print("\n",text[j][i]," ", sep ="", end = "", file=fOut)
            length = len(text[j][i])
        else:
            print(text[j][i]," ", sep="", end="", file=fOut)
            length+=1
    
fOut.close()

##Read in file, store in array
#fOut = open(newName, "r")
#lines= fOut.readlines()
#fOut.close()

##Remove trailing spaces, write to file
#fOut = open(newName, "w")
#for i in range(len(lines)):
    #print(lines[i].strip(), file = fOut)
#fOut.close()