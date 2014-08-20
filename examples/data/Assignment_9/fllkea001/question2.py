#Keanon Fell
#Computer Science assignment 9 
#11 May 2014

#Formatting the data in a text file into a paragraph format

outputStr = ""

#Prompting user for input
print("Enter the input filename:")
filename = input()
print("Enter the output filename:")
newFile = input()
print("Enter the line width:")
width = int(input())

#Reading data into string variable
inputFile = open(filename, "r")
newString = inputFile.read()
inputFile.close()

#Formatting string into the desired output
stringLength = len(newString)
index = stringLength
start = 0
end = width

#Tring to first print the characters in lines of width enterd
while index > 0:
    if index > width:
        outputStr = outputStr + "" + newString[start:end] + "\n"
        start = start + width
        end += width
        index = index - width
    elif index < width:
        outputStr = outputStr + "" + newString[start:stringLength]

#Writing to the file
f = open (newFile, "w")
print ("print (\"" + outputStr + "\)", file=f)
f.close ()