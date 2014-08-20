""" Program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT.
Telisha Ramlall
20 April 2014"""

labels = ["1 ", "2+", "2-", "3 ", "F "]
counters = ['', '', '', '', '']

marks = input("Enter a space-separated list of marks:\n").split() #converting input string into array

for i in range(len(marks)): #convert string values to integers
    marks[i] = eval(marks[i])

#check which category each mark falls in and add X to that category
for mark in marks: 
    if mark >= 75:
        counters[0] += "X"
    elif mark >= 70:
        counters[1] += "X"
    elif mark >= 60:
        counters[2] += "X"
    elif mark >= 50:
        counters[3] += "X"
    else:
        counters[4] += "X"
        
for i in range(len(labels)):
    print(labels[i], "|", counters[i], sep = "") #print labels array and counter array
        
