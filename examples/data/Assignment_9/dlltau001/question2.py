"""Question 2
Assignment 9
Tauriq Dolley

Write a program to reformat a text file so that all lines are at most a given length"""

words = []
file = input("Enter the input filename:\n")
f = open(file,"r")

newfile = input("Enter the output filename:\n")
nf = open(newfile,"w")

width = eval(input("Enter the line width:\n"))

for lines in f:
    for word in lines.split(" "):
        words.append(word.strip("\n"))
        
f.close()
    
count = 0
for word in words:             
        
    if (count + len(word)) <= width:    #if adding this word doesn't amount to the width print word with space
        nf.write((word+" "))
        count = count + (len(word) +1)           
        
    elif (count + len(word)) > width :                           #if adding word exceeds width limit, next line, reset count and print word and add character count        
        nf.write("\n")
        count = 0
        nf.write((word+" "))
        count = count + (len(word) + 1)    

nf.close()

