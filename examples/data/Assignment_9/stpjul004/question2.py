""" Program to adjust the width of text in a file
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-05-16 """

# Ask the user to specify input and output filenames
inputFileName = input("Enter the input filename:\n")

outputFileName = input("Enter the output filename:\n")

# Ask the user to specify a line width
lineWidth = eval(input("Enter the line width:\n"))

# Attempt to open the input file
try:
    inputFile = open(inputFileName, "r")
    lines = inputFile.readlines()
    inputFile.close()
except IOError as error:
    print("No file found!\n Error produced:",error)

new_lines = []

for i in range(len(lines)):
    if len(lines[i]) <= lineWidth:
        newlines.append(lines[i])
    else:
        tempstr = ''
        words = lines.splitlines(' ')
        i = 0
        while len(tempstr)

for i in new_lines:
    print(i)