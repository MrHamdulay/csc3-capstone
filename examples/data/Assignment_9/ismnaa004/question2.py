'''Naadirah Ismail program to fir text in given width'''
inFile = open(input("Enter the input filename:\n"),"r")
lines = inFile.readlines()
inFile.close()

width = eval(input("Enter the line width:\n"))
allWords = []

for line in lines:
    words = line.split(" ")
    for word in words:
        word = word.replace("\n","")
        if word == "":
            continue
        allWords.append(word)
        
lengthWords = 0
editedText = ""
    
for word in allWords:
    lengthWords += len(word) + 1
    if lengthWords > width:
        editedText += "\n" + word + " "
        lengthWords = len(word)
    else:
        editedText += word + " "
        
newFilename = input("Enter the output filename:\n")      
writeOutFile = open(newFilename,"w")  
writeOutFile.write(editedText)
writeOutFile.close()
