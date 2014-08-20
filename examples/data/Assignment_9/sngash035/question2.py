#Program to format text file into a paragraph according to given line length 
#Ashton Singh
#18 May 2014

choicein= input("Enter the input filename:\n")
choiceout = input("Enter the output filename:\n")
inputf = open(choicein, "r")
outputf = open(choiceout, "w")
width = eval(input("Enter the line width:\n"))
string = inputf.read()
x = string.splitlines(True)
string = "".join(x)

outputText = string.split("\n\n")
for i in range(len(outputText)): #first iteration 
    outputText[i] = outputText[i].replace("\n", " ")

formatted_outputText = []
for iteration in outputText:#second iteration
    iteration = iteration.split(" ")
    new_string = []
    count = 0
    
    for o in iteration: #runs through each word in the paragraph (outputText)
        if count + int(len(o)) <= width:   
            new_string.append(o)
            new_string.append(" ")
            count+= int(len(o)+1)
        
        else:
            new_string.append("\n")  #ensure that words are not seperated or split
            count = 0
            new_string.append(o)
            new_string.append(" ")
            count+= int(len(o)+1)
            
    formatted_outputText.append(new_string)

for j in formatted_outputText:
    if j[-1] == " ":
        j[-1] = ""
    else:
        continue

for iteration in formatted_outputText:#third iteration
    string = "".join(iteration)
    string = string + "\n"
    print(string, file=formatted_outputText)
    
    
inputf.close() 
outputf.close() #close both text files to prevent errors 
