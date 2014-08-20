# Name: Aaron Weinstein
# Student Number: wnsaar001
# Date: 2014/02/25



hour =eval(input("Enter the hours: \n"))
minute =eval(input("Enter the minutes: \n"))
second = eval(input("Enter the seconds: \n"))
count =0
if hour > 24:
    count = count + 1
if hour < 0:
    count = count + 1
if minute > 59:
    count = count + 1
if minute < 0:
    count = count + 1
if second > 59:
    count = count + 1
if second < 0:
    count = count + 1    

if count  > 0:
    print("Your time is invalid.")
if count  < 1:
    print("Your time is valid.")
    