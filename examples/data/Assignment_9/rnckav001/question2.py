#assignment 9 Q2 - reformatting files
#Kavir Ranchod RNCKAV001
#14/05/2014

#Get input file, output file, and line length
oldfile = input("Enter the input file name:\n")
newfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#save the file contents in "lines"
f = open(oldfile, "r")
lines = f.readlines()
f.close()

#remove last "\n" character from each line
for i in range(len(lines)-1):
    lines=lines[i][:-1]

alllines=[]
LineNo = 0

#paragraph checking
for i in range(len(lines)):
    if lines[i] == "":
        alllines.append("\n\n")
    else:
        alllines.append(lines[i].split(" "))

#transfer content of file to a new file, with it starting on a new line each time it is close to or equals the variable "width"
f = open(newfile, "w")
for i in range(len(alllines)):
    for j in range(len(alllines[i])):
        if LineNo == 0:
            LineNo = (len(alllines[i][j]) + 1)
            print(alllines[i][j], end=" ", file = f)
        elif alllines[i][j] == "\n\n":
            LineNo = 0
            print(alllines[i][j], sep = "", end = "", file = f)
        elif (len(alllines[i][j]) + LineNo) > width:
            print("\n",alllines[i][j], sep = "", end = " ", file = f)
            LineNo = len(alllines[i][j] + 1)
f.close()