'''Assign9,Q2 reformating text from a text file
Kieran Reilly, RLLKIE001
13/05/14'''
    


string = ""     #used in storing the text
inFile = input("Enter the input filename:\n")
f = open(inFile, "r")   #opens file
string = f.read()       #stores text in a string
f.close()               #closes file

outFile = input("Enter the output filename:\n")

width = int(input("Enter the line width:\n"))


words = string.split(" ")   #splits string into a list of words
string = ""                 #resets the value of the string to "" for later use
for i in range(len(words)): #used in order to check for the "\n" in the string
    if len(words[i]) > 2:
        if words[i][:1] == "\n":
            words[i] = words[i][1:]
        elif words[i][-1:] == "\n":
            words[i] = words[i][:-1]
    elif len(words[i]) == 2 and words[i] == "\n":
        words[i] = ""
    string = string + " " + words[i]

string = string[1:]
outString = ""
#outString = formatting(string, width, outString)

count = 0
lines = []
chopped = ""
for i in range(len(string)):
    
    if count < width+1:
        outString = outString + string[i]
    elif count == width+1:
        if outString[len(outString)-1] != " ":
            space = ""
            n = 1
            while space == "":
                space = outString[(len(outString)-1)-n]
                n+=1
            outString = outString[:(len(outString)-1)-n] + " "*n
            chopped = string[i-n:i]
            lines.append(outString)
            outString = ""
            outString = chopped.strip()
            count = n
            
        elif outString[len(outString)-1] == " ":
            lines.append(outString)
            outString = ""
            count = 0
    count += 1    
            
            
for i in range(len(lines)):
    print(lines[i])
            
    
    
    
    
    
    
    
    
    
    
    
    '''if count == width:
        if outString[len(outString)-1] != " ":
            space = ""
            n = 1
            while space == "":
                n += 1
                space = outString[len(outString)-n]
            outString = outString[:i-n] + " "*n
            chopped = string[n:i]
            print(chopped)
            lines.append(outString)
            outString = chopped
            count = len(outString)
        else:
            lines.append(outString)
            outString = ""
            count = 0


for i in range(len(lines)):
    print(lines[i])'''
        
        