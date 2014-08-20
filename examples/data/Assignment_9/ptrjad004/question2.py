"""formats file to specified line width
Jade Petersen
Assignemnt 9
Question 2
15 May 2014"""

inp_file = input("Enter the input filename:\n")
out_file = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))

infile = open(inp_file, 'r')
lines = infile.read()
infile.close()

#create a list with paragraphs
lines = lines.split("\n\n")
output = open(out_file, "w")
for i in lines:
    i = i.replace("\n"," ")
    i = i.split(" ") #creating a list of words
    count=-1
    for word in i:
        count+=len(word)+1
        if count <= line_width:
            print(word,file=output,end= " ")
        else:
            print(file=output)
            print(word,file=output,end=" ")
            count = len(word)
    print(file=output)
    print(file=output)
output.close()
    

