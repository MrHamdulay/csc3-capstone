"""question 2
clare walker
11 May 2014"""
#get inputs
infile=open(input("Enter the input filename:\n"), "r")
outfile=open(input("Enter the output filename:\n"), "w") 

#get data from input file
whole_message=infile.read()
infile.close()
width=eval(input("Enter the line width:\n"))
splitparas=[]
start=0
#split the whole message into a list in which each item is a paragraph

for i in range(0,(len(whole_message)-4)):
    if whole_message[i:i+2] == "\n\n":
        splitparas.append(whole_message[start:i])
        start = i+2
        
    else:
        continue
splitparas.append(whole_message[start:-1])
#for each item/string in list, replace newline characters with a space
noNewLine=[]
for i in range(len(splitparas)):
    noNewLine.append(splitparas[i].replace("\n", " "))
            
#finally process list, one string at a time, to get final output
outputparas=""            
for i in range(len(noNewLine)):
    # convert each paragraph to a list
    words=noNewLine[i].split(' ')
    #add first word to paragraph
    newpara=words[0]
    #add rest of the words
    lineLength =len(words[0])
    for i in range(1, len(words)):
        
        if (lineLength+len(words[i])+1) > width: #if adding a word would exceed width limit, add a newline character before word is added
            newpara=newpara+"\n"+words[i]
            lineLength =len(words[i])
        else:
            newpara=newpara+' '+words[i]
            lineLength+=(len(words[i])+1)
    # add each paragraph to output, each separated by a line
    outputparas=outputparas+newpara+"\n\n"
    

print(outputparas, file=outfile)
outfile.close()    