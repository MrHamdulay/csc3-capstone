"""
Assignment 6 - Question 4
Program to produce histogram from inputted marks
Jayan Smart
April 2014
"""

#Recieve marks from user:
marks = input("Enter a space-separated list of marks:\n")
marks = marks.split(' ')
for i in range(len(marks)):
    marks[i] = eval(marks[i])

#Catagorise marks into mark catagories:
first = []
second_high = []
second_low = []
third = []
fail = []
valid = True
for j in range(len(marks)):
    if marks[j] < 0:
        print('Invalid mark - ', marks[j])
        valid = False
    elif marks[j] < 50:
        fail.append(marks[j])
    elif marks[j] < 60:
        third.append(marks[j])
    elif marks[j] <70:
        second_low.append(marks[j])
    elif marks[j] <75:
        second_high.append(marks[j])
    elif marks[j] <101:
        first.append(marks[j])
    else:
        print("Invalid mark -", marks[j])
        valid = False

#Print histogram of marks:
if valid == True:
    print("1 |"+"X"*len(first))
    print("2+|"+"X"*len(second_high))
    print("2-|"+"X"*len(second_low))
    print("3 |"+"X"*len(third))
    print("F |"+"X"*len(fail))
