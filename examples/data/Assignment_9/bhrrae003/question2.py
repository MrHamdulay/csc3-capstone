inputfile = input("Enter the input filename:\n")
outputfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

in_file = open(inputfile, 'r')
file_lines = in_file.read()
in_file.close()


lines = file_lines.split("\n\n")
output = open(outputfile, "w")
for i in lines:
    i = i.replace("\n"," ")
    i = i.split(" ") 
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
    

