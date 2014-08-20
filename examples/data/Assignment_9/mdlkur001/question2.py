"""kureshlen moodley
mdlkur001
16 may 2014"""

choicei= input("Enter the input filename:\n")
choiceo = input("Enter the output filename:\n")
inputf = open(choicei, "r")
outputf = open(choiceo, "w")
width = eval(input("Enter the line width:\n"))
string = inputf.read()
x = string.splitlines(True)
string = "".join(x)

paragraph = string.split("\n\n")
for i in range(len(paragraph)): #first iteration
    paragraph[i] = paragraph[i].replace("\n", " ")

formatted_paragraph = []
for iteration in paragraphs:#second iteration
    iteration = iteration.split(" ")
    new_string = []
    count = 0
    
    for o in iteration: #j runs through each word in the paragraph
        if count + int(len(o)) <= width:   #if a word is too short
            new_string.append(o)
            new_string.append(" ")
            count+= int(len(s)+1)
        
        else:
            new_string.append("\n")  #to ensure that words stay whole at the end of lines
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

for iteration in formatted_paragraph:#third iteration
    string = "".join(iteration)
    string = string + "\n"
    print(string, file=output_file)
    
    
inputf.close()
outputf.close()
