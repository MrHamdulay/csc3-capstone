#Program to determine whether a year is a leap year or not
#Illustrates use of math library.
#Michell Ndlozi
#NDLMIC004
# 2014/03/08
def year(x): #everything under here is defining the function 
    if ((x%400==0) or (x%4==0) and (x%100!=0)): 
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")
x=eval(input("Enter a year:\n"))   #first define the function and then give the variable
year(x)   #call function to envoke it automatically
