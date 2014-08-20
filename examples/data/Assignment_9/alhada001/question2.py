#Adam Alhadeff
fileName = input("Enter the input filename:\n")
newFileName = input("Enter the output filename:\n")
width = input("Enter the line width:\n")
lineWidth = int(width)

inputFile = open(fileName, "r")
s = inputFile.read()
splitting_String = s.replace("\n\n","NEWPARAGRAPHHERE").replace("\n"," ").replace("NEWPARAGRAPHHERE","\n\n").split(" ")
inputFile.close()


outfile = open(newFileName, "w")
counter = 0


for i in range(len(splitting_String)):
    number = len(splitting_String[i])
    counter = counter + 1 + number   
    
    if "\n\n" in splitting_String[i]:
        array_temp = splitting_String[i].split("\n\n")
        counter = len(array_temp[1])
        print (splitting_String[i],"",end = "",file = outfile)    
   
    elif counter <= lineWidth:
        print (splitting_String[i],"",end = "",file = outfile)
    elif counter > lineWidth:
        print("\n",splitting_String[i],sep = "",end = " ",file = outfile)
        counter = len(splitting_String[i])
        
outfile.close()