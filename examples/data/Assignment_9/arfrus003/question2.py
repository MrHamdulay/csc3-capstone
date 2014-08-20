inputfile = input("Enter the input filename:\n")
outputfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

infile = open(inputfile, 'r')
lines = infile.read()
infile.close()

#create a list with paragraphs
lineslist = lines.split("\n\n")
output = open(outputfile, "w")
for i in lineslist:
    i = i.replace("\n"," ")
    i = i.split(" ") #creating a list of words
    count=-1
    for word in i:
        count+=len(word)+1
        if count <= width:
            print(word,file=output,end= " ")
        else:
            print(file=output)
            print(word,file=output,end=" ")
            count = len(word)
    print(file=output)
    print(file=output)
output.close()
    

