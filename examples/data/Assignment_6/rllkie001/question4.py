#Kieran Reilly, RLLKIE001
#HistogramMarkCreater
#Assignment 6, question 4
#23/04/14

marks = []

fail = ""
third = ""
lowerSecond = ""
upperSecond = ""
first = ""

enteredMarks = input("Enter a space-separated list of marks:\n")
marks = enteredMarks.split(" ")

marks.sort()

for i in range(len(marks)):
    marks[i] = int(marks[i])
    
for i in range(len(marks)):
    if(marks[i] < 50):
        fail = fail + "X"
    elif(marks[i] >= 50 and marks[i] < 60):
        third = third + "X"
    elif(marks[i] >= 60 and marks[i] < 70):
        lowerSecond = lowerSecond + "X"
    elif(marks[i] >= 70 and marks[i] < 75):
        upperSecond = upperSecond + "X"
    else:
        first = first + "X"
        
print("1 |"+first)
print("2+|"+upperSecond)
print("2-|"+lowerSecond)
print("3 |"+third)
print("F |"+fail)