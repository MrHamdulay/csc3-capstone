#Kiuran Naidoo
#Assignment 9
#Question 2

import textwrap

fileInput = input("Enter the input filename:\n")
fileOutput = input("Enter the output filename:\n")
lineWidth = eval(input("Enter the line width:\n"))
currentString = ""
outString = []
inFile = open(fileInput,"r")
outFile = open(fileOutput,"w")

for line in inFile:
 if line != "\n":
  currentString += line
 else:
  outString = textwrap.wrap(currentString,lineWidth)
  for i in range(len(outString)):
   print(outString[i],file=outFile)
  print("",file=outFile)
  currentString = ""
if currentString != "":
  outString = textwrap.wrap(currentString,lineWidth)
  for i in range(len(outString)):
   print(outString[i],file=outFile)
 
inFile.close()
outFile.close()
 
 