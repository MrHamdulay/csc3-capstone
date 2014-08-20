"""Program that reformats a text file so that all lines are at most a given length
Matthew Finlayson - FNLMAT001
11/05/2014"""

inputFile = input ("Enter the input filename:\n")

outputFile = input ("Enter the output filename:\n")

lineWidth = eval(input("Enter the line width:\n"))

# code to determine how many lines are in the file
f = open(inputFile, "r")
line = f.readline()
numLines = 1
while f.readline() != "":
    numLines += 1
f.close()


iFile = open (inputFile, "r")
oFile = open (outputFile, "w")

outputString = "" # keeps track of each line to be printed to the output file
lastWordPrinted = False

for j in range(numLines):
    line = iFile.readline() # reads each line
    line = line[:-1] # removes the \n character from each line
    
    if(line == ""): # if the input line is blank
        print(outputString, file = oFile)
        outputString = ""
        print("",file = oFile)
        
        
    else: # input line is not blank
        words = line.split(" ") # creates list of all the words in each line
        for i in range(len(words)):
            if (len(outputString) + len(words[i]) + 1 <= lineWidth): # if the width is still less once the new word is added
                #if words[i] == "": # if there is an empty strings it means there was a double space 
                #    outputString += " " # add extra space
                if len(outputString) == 0: # if the word added is on a new line
                    outputString = words[i]
                else:
                    outputString = outputString + " " + words[i] 
                   
            else: # the width of outputString is too large if the new word is to be added
                if (i == len(words)-1 and j == numLines-1): # if the current word is the last one of the file
                    print(outputString, file = oFile) # print the full line onto the output file
                    lastWordPrinted = True
                    print(words[i], file = oFile) # create the line with only that word
                else:
                    print(outputString, file = oFile) # print the full line onto the output file
                    outputString = words[i] # add the new word onto the next line
                    
            if (i == len(words)-1 and j == numLines-1 and lastWordPrinted == False): # if the current word is the last one of the file
                print(outputString, file = oFile)        
        

iFile.close()
oFile.close()