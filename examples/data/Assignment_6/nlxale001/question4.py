#Author: NLXALE001
#Date:23 April 2014
#Assignment 6

marks = input("Enter a space-separated list of marks:\n")
marks = marks.split(" ")

#count number of each section
countone = 0
counttwoplus = 0
counttwominus = 0
countthree = 0
countf = 0
for i in range (0, len(marks)):
    if eval(marks[i]) < 50:
        countf += 1
    elif eval(marks[i]) < 60:
        countthree += 1
    elif eval(marks[i]) < 70:
        counttwominus += 1
    elif eval(marks[i]) < 75:
        counttwoplus += 1
    else:
        countone += 1
#print results
print ("1 |", "X"*countone, sep="")
print ("2+|", "X"*counttwoplus, sep="")
print ("2-|", "X"*counttwominus, sep="")
print ("3 |", "X"*countthree, sep="")
print ("F |", "X"*countf, sep="")

