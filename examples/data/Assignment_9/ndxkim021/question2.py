#Program to format a text file into a paragraph according to the stipulated line length
#Kimberley Naidoo
#17 may 2014

filein= input("Enter the input filename:\n")
fileout = input("Enter the output filename:\n")
inputf = open(filein, "r")
outputf = open(fileout, "w")
linelength = eval(input("Enter the line width:\n"))
string = inputf.read()
x = string.splitlines(True)
string = "".join(x)

para = string.split("\n\n")
for i in range(len(para)): #iteration 1
    para[i] = para[i].replace("\n", " ")

formatted_paragraph = []
for iteration in paragraphs:# iteration 2
    iteration = iteration.split(" ")
    new_string = []
    count = 0
    
    for o in iteration: #loop goes through each word added to the paragraph so far
        if count + int(len(o)) <= linelength:   
            new_string.append(o)
            new_string.append(" ")
            count+= int(len(s)+1)
        
        else:
            new_string.append("\n")  #making sure no words are seperated
            count = 0
            new_string.append(o)
            new_string.append(" ")
            count+= int(len(o)+1)
            
    formatted_paragraph.append(new_string)

for j in formatted_paragraph:
    if j[-1] == " ":
        j[-1] = ""
    else:
        continue

for iteration in formatted_paragraph:# iteration 3
    string = "".join(iteration)
    string = string + "\n"
    print(string, file=outputf)
    
    
inputf.close()
outputf.close()
