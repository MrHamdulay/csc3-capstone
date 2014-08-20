"""Program to reformat a text file
Axel du Plessis
16/05/2014"""

inFile = open(input("Enter the input filename:\n"),"r")
lines = inFile.readlines()
inFile.close()

newFilename = input("Enter the output filename:\n")  
width = eval(input("Enter the line width:\n"))

lengthWords = 0
editedText = ""

for line in lines:
    if line == "\n":
        editedText += "\n\n"
        lengthWords = 0
    else:
        words = line[:-1].split(" ")
        for word in words:
            lengthWords += len(word)
            if lengthWords > width:
                editedText += "\n" + word + " "
                lengthWords = len(word) + 1
            elif lengthWords == width:
                editedText += word + "\n"
                lengthWords = 0
            else:
                editedText += word + " "
                lengthWords += 1
    
            
writeOutFile = open(newFilename,"w")  
writeOutFile.write(editedText)
writeOutFile.close()