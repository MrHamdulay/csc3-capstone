# question4.py
# A program that creates a histogram based on the UCT grading system
# Martin Batek
# BTKMAR001
# 22 April 2014

fail = 0
third = 0
lowsecond = 0
hisecond = 0
first = 0

marks = input("Enter a space-separated list of marks:\n")
listofmarks = marks.split(" ") # arranges marks into list

for i in range(len(listofmarks)):
    listofmarks[i] = eval(listofmarks[i]) # converst marks from strings to numbers
    
for mark in listofmarks: # tests for which category each mark fits into
    if mark < 50:
        fail += 1
    elif 50 <= mark < 60:
        third += 1
    elif 60 <= mark < 70:
        lowsecond += 1
    elif 70 <= mark < 75:
        hisecond += 1
    elif mark >= 75:
        first += 1
        
print("1","|"+("X"*first))
print("2+"+"|"+("X"*hisecond))
print("2-"+"|"+("X"*lowsecond))
print("3","|"+("X"*third))
print("F","|"+("X"*fail))
    
# draws a histogram