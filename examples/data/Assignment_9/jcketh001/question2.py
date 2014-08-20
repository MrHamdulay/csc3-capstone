#Program to reformat text file
#Ethan Jackson
#14 May 2014

words =[]
rowLength = 0
output=''
i=1

#length = 40
#outputName='output.txt'

filename = input("Enter the input filename:\n")

outputName = input("Enter the output filename:\n")#inputs by user
length = eval(input("Enter the line width:\n"))

f = open(filename, "r")
readfile = f.readlines()
f.close()

f = open(outputName, "w")

for i in readfile:#runs thorugh the names and marks
    i=i.replace('"','')#removes the quotation marks
    words+= i.split(" ")#splits each word by a space
#print(words)

output=words[0]
rowLength=len(output)

for i in range(1,len(words)):
    if (rowLength+len(' '+words[i]))<length:#checks how many words can fit on a line
        output+=' '+words[i]
        rowLength+=len(' '+words[i])
    else:
        output+='\n'+words[i]
        rowLength=len(words[i])
print(output, file = f)
f.close()
#print (output)

#f = open(outputName,"w")#creates the output file as a new renamed file
#print(output, file=f)
#f.close()

