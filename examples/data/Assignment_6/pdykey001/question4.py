"""Keyoolin Padayachee
Histogram
24 April 2014"""

marks = input("Enter a space-separated list of marks:\n").split(" ")
first = 0
secondP = 0
secondM = 0
third = 0
fail = 0
for i in range(len(marks)):
    mark = eval(marks[i])
    if mark>=75:
        first+=1
    elif mark>=70:
        secondP+=1
    elif mark>=60:
        secondM+=1
    elif mark>=50:
        third+=1
    else: 
        fail+=1
print("1 |"+"X"*first)
print("2+|"+"X"*secondP)
print("2-|"+"X"*secondM)
print("3 |"+"X"*third)
print("F |"+"X"*fail)
        