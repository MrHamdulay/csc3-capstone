# Question 3, Assignment 9, Sudoku Checker
# Michael Sanne
# 2014/05/10

import sys
# Function to find first space in a string
def findSpace (reader, width):
    for i in range (width-1, 0, -1):
        if (reader[i] == " "):
            return i
        else:
            continue
# Finds and creates len of width lines      
def formatting (string):
    lining = []
    string = string.replace ("\n", " ")
    while (string):
        # Checks for spaces to avoid breaking up a word
        if (len(string) <= width-1):
            lining.append(string)
            break
        else:
            if (string[width] == " "):
                lining.append(string[0:width])
                string = string[width+1:]                
            else:
                space = findSpace (string, width)
                lining.append (string[0:space])
                string = string[space+1:]    
    return lining

#Main method
def main (fileInput, fileOutput, width):
    #Reads File
    file = open(fileInput, "r")
    read = file.readlines()
    reader = ""
    
    for i in range (len(read)):
        reader += read[i]
    file.close()
            
    #Splits it into paragraphs
    lines = []
    readerL = reader.split("\n\n")
    print (readerL)
    for i in range (len(readerL)):
        lines.append(formatting(readerL[i]))
    file = open (fileOutput, "w")    
    # Write to file
    
    for i in range (len(lines)):
        for j in range (len(lines[i])):
            file.write(lines[i][j] + "\n")
        file.write("\n")
    file.close()    
  
#User Input and Starts main method 
fileInput = input("Enter the input filename:\n")
fileOutput = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

main (fileInput, fileOutput, width)
