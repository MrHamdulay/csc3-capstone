"""Ricky Conn
CNNRIC004
Allows for text wraping of a file where the user is able to input the maximum
line width and writes it to a file"""

#Enter read and write file names.
RFileName = input("Enter the input filename:\n")
WFileName = input("Enter the output filename:\n")
lineWidth = eval(input("Enter the line width:\n"))

#creates an array with all lines of text file input
lines = open(RFileName, "r")
lines = lines.readlines()
totalString = ""
lineString = ""
lcounter = 0

#loops through each line of the text file
for line in lines:
    #Keeps track of which line it is dealing with
    lcounter += 1
    wcounter = 0
    #Creates Array of words in line
    lineA = line.split(" ")
    #if its the same paragraph
    if(line != "\n"):
        for word in lineA:
            #Keeps track of the the position of the word (number of word)
            wcounter +=1
            #If it is the last line and the last word
            if((lcounter == len(lines))and(wcounter == len(lineA))):
                #if when you add another word with a space it is bigger than the chosen line width
                #Put the current word on a new line otherwise add the word to the total string
                if(len(lineString)+len(word)+1  > lineWidth):
                    totalString += lineString + "\n" + word
                    lineString = ""   
                else:
                    totalString += lineString + " " + word
            else:
                #if the current line does not indicate a new paragraph and the word is the last woprd in the line
                if((line != "\n") and (word[len(word)-1:]== "\n")):
                    word = word[:len(word)-1]
                #if when you add another word with a space it is bigger than the chosen line width
                #add the line to the total string and make the new line black (start a new line)
                if(len(lineString)+len(word)+1  > lineWidth):
                    totalString += lineString + "\n"
                    lineString = ""
                #If it is the start of the new line add the word with no space infront of it and if it is not
                #add a the word to the string with a space infront of it
                if(lineString != ""):
                    lineString += " " + word
                else:
                    lineString += word 
                    
    #If it is a new paragraph add a black line to the total string
    else:
        totalString += lineString + "\n\n"
        lineString = ""
        
#Write the total string to the chosen file name    
wfile = open(WFileName, "w")      
print(totalString, file = wfile)
