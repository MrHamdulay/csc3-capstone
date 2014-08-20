'''Assignment 6 question 4 Histogram of Marks
Adam Smith
23 April 2014'''

import shlex 

marks = shlex.split(input("Enter a space-separated list of marks:\n")) #stores marks in a list

First = UpperSecond = LowerSecond = Third = Fail = 0

for i in range (len(marks)): #runs through list and finds if the marks are Firsts, UpperSeconds, LowerSeconds etc.
    mark = eval(marks[i])
    
    if mark >= 75:
        First +=1
    elif mark >= 70:
        UpperSecond +=1
    elif mark >= 60:
        LowerSecond +=1
    elif mark >= 50:
        Third +=1    
    else:
        Fail +=1
        
print("1 |" + "X"*First) #Prints the Histogram
print("2+|" + "X"*UpperSecond)
print("2-|" + "X"*LowerSecond)
print("3 |" + "X"*Third)
print("F |" + "X"*Fail)