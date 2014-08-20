#Assignment 2
#Question 1
#Determing a leap year

x = eval(input("Enter a year:\n"))
if x%400 ==0:
    print(x, "is a leap year.", sep=" ")
elif x%4==0 and x%100!=0:
    print(x, "is a leap year.", sep=" ")
else:
    print(x, "is not a leap year.", sep=" ")

