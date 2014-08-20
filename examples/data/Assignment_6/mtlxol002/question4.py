"""CSC1015F Assignment 6 Question 4
Xola Matlanyane MTLXOL002
25 April 2014"""

axis = ["1 ", "2+", "2-", "3 ", "F "]
spaces = ['', '', '', '', '']

markinp = input("Enter a space-separated list of marks:\n").split() #converting input string into array

for i in range(len(markinp)): #convert string values to integers
    markinp[i] = eval(markinp[i])

#check which category each mark falls in and add X to that category
for mark in markinp: 
    if mark >= 75:
        spaces[0] += "X"
    elif mark >= 70:
        spaces[1] += "X"
    elif mark >= 60:
        spaces[2] += "X"
    elif mark >= 50:
        spaces[3] += "X"
    else:
        spaces[4] += "X"
        
for i in range(len(axis)):
    print(axis[i], "|", spaces[i], sep = "") #print labels array and counter array