"""program to reformat a text file
tayla george
15 may 2014"""


input_fn = input("Enter the input filename:\n")
output_fn = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

inputfile=open(input_fn,"r")         #opening the input file so that it can be read
outputfile=open(output_fn,"w")       #opening the output file for overwriting

                                     #process each line of the inputfile
lines = inputfile.readlines()        #creates a list with each line as an item
inputfile.close()                    #closing the input file
count=-1                             #initializing a counter
for line in lines:
    if line!='\n' :
        line=line.replace('\n','')   #removes the newline character
        line=line.split(' ')         #splitiing the line into words
        for word in line:
            count+=len(word)+1       # +1 includes the character after the word
            if count <= width:
                print(word,file=outputfile,end=' ')
            else:
                print(file=outputfile)
                print(word,file=outputfile,end=' ')
                count=len(word)
    else:
        line=line                    #provides for printing it into separate paragraphs
        print(file=outputfile) 
        print(file=outputfile)
        count=-1
outputfile.close()
