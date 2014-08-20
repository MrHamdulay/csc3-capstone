"""Assignment 9 Question 2
16 May 2014 Djavan Arrigone"""

lists = []
inputf = input("Enter the input filename: \n")
outputf = input("Enter the output filename: \n")
lwidth = eval(input("Enter the line width: \n"))
lenwords = 0

inf = open(inputf, "r") #read from file
lists = inf.readlines()
inf.close()

for i in range(len(lists) - 1): #remove \n
    lists[i] = lists[i][:-1]

entries = []

for i in range(len(lists)): #to effectively deal with paragraph lines. 
    if lists[i] == "":
        entries.append(["\n\n"])
    else: 
        entries.append(lists[i].split(" "))
    

outf = open(outputf, "w") #open writing file

for i in range(len(entries)): #Nested forloop dealing with formatting text. 
    for j in range(len(entries[i])):
        
        if lenwords == 0:
            
            lenwords = len(entries[i][j]) + 1
            print(entries[i][j], end=" ", file = outf)
        elif entries[i][j] == "\n\n":
           
            lenwords=0
            print(entries[i][j], sep="", end="", file = outf)
        elif len(entries[i][j]) + lenwords > lwidth:
           
            print("\n",entries[i][j],sep="",end=" ", file = outf)
            lenwords = len(entries[i][j]) + 1
        else:
            
            if len(entries[i][j]) + lenwords <= lwidth:
                
                lenwords = lenwords + len(entries[i][j]) + 1
                print(entries[i][j], end=" ",file = outf)
            else:
               
                print(entries[i][j], end="",file = outf)

outf.close()