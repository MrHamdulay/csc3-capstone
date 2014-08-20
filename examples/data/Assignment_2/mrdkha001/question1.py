# Question 1
# Name: Khanyisile Morudu
# Student Number: mrdkha001
# Date: 07/03/2014

def LeapYear_Check(n):
    if ((n%400) == 0) or ((n%4 ==0) and (n%100 != 0)):
        print(str(n), "is a leap year.")
    else:
        print(str(n), "is not a leap year.")
    
    
year = eval(input("Enter a year: \n"))
LeapYear_Check(year)