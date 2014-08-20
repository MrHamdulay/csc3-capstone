'''Assignment 9 question 2 Line width editor
Adam Smith
12 May 2014'''

InputName = input("Enter the input filename:\n") #get file names
OutputName = input("Enter the output filename:\n")
LineWidth = eval(input("Enter the line width:\n"))

lines = []
words = []
CurrentWidth = 0
OutputString = ""

f = open(InputName, "r") #read input file
lines = f.readlines()
f.close()

for line in lines: #if the line is a paragraph make it spaces otherwise remove the new line character
    if line != "\n":    
        line = line[:-1]
        words = words + line.split(" ")
    else:
        line = " "*LineWidth
        words.append(line)
        
for word in words: # calculate if the current word can fit on the line or if it has to be moved to the next
    if CurrentWidth + len(word) < LineWidth:
        OutputString += word + " "
        CurrentWidth += len(word) + 1
    elif CurrentWidth + len(word) == LineWidth:
        OutputString += word + "\n"
        CurrentWidth = 0
    else:
        OutputString += "\n" + word + " "
        CurrentWidth = len(word) + 1

f = open(OutputName, "w") #print to the output file
print(OutputString, file = f)
f.close()