filein = open (input("Enter the input filename:\n"), "r")
lines = filein.readlines()
filein.close()
fileOut = open(input("Enter the output filename:\n"),"w")
width = eval(input("Enter the line width:\n"))
finalFormattedString=""
linecount= 0
currentlineinprogress = ""
for currentline in lines:
    wordcount=0    
    linecount += 1
    currentlinearray = currentline.split(" ")
    if(currentline != "\n"):
        for word in currentlinearray:
            wordcount+=1
            if linecount == len(lines) and wordcount == len(currentlinearray):
                if len(currentlineinprogress) + len(word) >= width:
                    finalFormattedString += currentlineinprogress +"\n" + word
                    currentlineinprogress = ""
                else:
                    finalFormattedString += currentlineinprogress +" " + word
            else:
                if word[-1] == "\n":
                    word = word[:-1]
                if len(currentlineinprogress) + len(word) >= width:
                    finalFormattedString += currentlineinprogress +"\n"
                    currentlineinprogress = ""
                if currentlineinprogress != "":
                    currentlineinprogress+= " "
                currentlineinprogress += word                
    else:
        finalFormattedString += currentlineinprogress + "\n\n"
        currentlineinprogress = ""          
print(finalFormattedString, file = fileOut)
fileOut.close()