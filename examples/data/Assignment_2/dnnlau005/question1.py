#Program to determine whether a year is a leap year or not (Assignment 2: Question 1)"
#Name: Lauren Denny
#Student Number: DNNLAU005
#Date: 10 March 2014

y=eval(input("Enter a year:\n"))
if y/400==y//400 or (y/4==y//4 and y/100!=y//100):
    print(y,"is a leap year.")
else:
    print(y,"is not a leap year.")
    