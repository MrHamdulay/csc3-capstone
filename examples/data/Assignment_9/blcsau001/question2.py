#Program to write a program to reformat a text file so that all lines are at most a given length.
#Saul Bloch
#14 May 2014

#Getting user input
fileName = input("Enter the input filename:\n")
newFileName = input("Enter the output filename:\n")
width = input("Enter the line width:\n")
lineWidth = int(width)

#Opening and reading file then closing file
inputFile = open(fileName, "r")
s = inputFile.read()
splitting_String = s.replace("\n\n","NEWPARAGRAPHHERE").replace("\n"," ").replace("NEWPARAGRAPHHERE","\n\n").split(" ")
inputFile.close()

#Opening the file to be written to
outfile = open(newFileName, "w")
counter = 0

#Using an almost bubble sort, replacing all the double returns with the 'newpar...' so that
#I can still find the new paragraphs (not losing the blank lines in between)

#Then replace all the single returns (simple new lines) with a space and put the double
#returns back and split on the space
for i in range(len(splitting_String)):
    number = len(splitting_String[i])
    counter = counter + 1 + number   
    #still being able to find the new paragraphs (not losing the blank lines in between)
    if "\n\n" in splitting_String[i]:
        array_temp = splitting_String[i].split("\n\n")
        counter = len(array_temp[1])
        print (splitting_String[i],"",end = "",file = outfile)    
    
    #Accountering for when the requested width is greater or less than the width of the file
    elif counter <= lineWidth:
        print (splitting_String[i],"",end = "",file = outfile)
    elif counter > lineWidth:
        print("\n",splitting_String[i],sep = "",end = " ",file = outfile)
        counter = len(splitting_String[i])
        
outfile.close()