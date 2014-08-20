# Question 2 - Assignment 9
# Oliver Harrison
# 13 May 2014

# Get input

in_name = input("Enter the input filename:\n")
out_name = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

# Add content of file to single string 

f = open(in_name, "r")
lines = f.read()
f.close()


# determine number of words
"""words = 1
for i in lines:
    if i == " ":
        words += 1 
    else:
        continue 

# create new list

newlines = []
for j in range(words):
    newlines.append([])"""
    
# add strings to new list
newlines = [[]]
y = 0
for x in lines:
    if x != " " and x != "\n":
        newlines[y].append(x)
    elif x == " ":
        newlines.append([])
        y += 1
    elif x == "\n":
        newlines[y].append(" ")

#print(newlines)

# Iterate through new list and print to file

f = open(out_name, "w")

current = 0
for i in range(len(newlines)):
    if (current + len(newlines[i])) > width:
        f.write("\n")
        for k in range(len(newlines[i])):
            f.write(newlines[i][k])
        f.write(" ")
        current = len(newlines[i]) +1
    else:
        for j in range(len(newlines[i])):
            f.write(newlines[i][j])
        f.write(" " )
        current += len(newlines[i]) +1

f.close()
