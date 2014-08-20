# Assignment 1 - Question 2
# Oliver Harrison
# 05 March 2013

def Time():
    hours=input("Enter the hours: \n")
    minutes=input("Enter the minutes: \n")
    seconds=input("Enter the seconds: \n")
    h=eval(hours)
    m=eval(minutes)
    s=eval(seconds)
    if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
Time()

