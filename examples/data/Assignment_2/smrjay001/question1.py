# Assignment 2 - Question 1
#07 March 2014
#Jayan Smart

x = eval(input("Enter a year:\n"))
r = x%4
c = x%400
v = x%100
if c == 0:
    print (x, 'is a leap year.')
elif r==0 and v != 0:
    print (x, 'is a leap year.')
else:
    print (x, 'is not a leap year.')