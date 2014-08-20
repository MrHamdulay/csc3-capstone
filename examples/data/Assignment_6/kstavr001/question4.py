"""Assignment 6,Question 4
Avreyna Kistensamy
20 April 2014"""

marks = input("Enter a space-separated list of marks:\n")

marks_list = marks.split(" ")

first = 0
second_upper = 0
second_lower = 0
third = 0
fail = 0

#putting grades into catergories
for mark in marks_list:
    if eval(mark) >= 75:
        first += 1
    elif 70 <= eval(mark) < 75:
        second_upper +=1
    elif 60 <= eval(mark) <70:
        second_lower += 1
    elif 50 <= eval(mark) < 60:
        third +=1
    else:
        fail +=1
        
#printing histogram
print("1 |", first*"X", sep="")
print("2+|", second_upper*"X", sep="")
print("2-|", second_lower*"X", sep="")
print("3 |", third*"X", sep="")
print("F |", fail*"X", sep="")

    
