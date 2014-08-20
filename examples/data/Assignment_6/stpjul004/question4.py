""" Program that displays the distribution of marks
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-24"""

#Get a list of space sperated marks
marks = input("Enter a space-separated list of marks:\n").split(" ")

#sort the marks from highest to lowest
marks.sort()
marks.reverse()

#change the strings into ints
for i in range(len(marks)):
    marks[i] = int(marks[i])

#sort the marks into categories
categories = [0,0,0,0,0] #[1,2+,2-,3,F]
for i in range(len(marks)):
    if marks[i] >=75:
        categories[0] += 1
    elif marks[i] >= 70:
        categories[1] += 1
    elif marks[i] >= 60:
            categories[2] += 1
    elif marks[i] >= 50:
            categories[3] += 1
    else: categories[4] += 1

#Display the historgram
print("1 |" + "X"*categories[0])
print("2+|" + "X"*categories[1])
print("2-|" + "X"*categories[2])
print("3 |" + "X"*categories[3])
print("F |" + "X"*categories[4])