#A program to determine whether it is a leap year or not.

x=(input("Enter a year:\n"))
x=int(eval(x))        

if (x%400==0) or (x%4==0) and (x%100!=0):
            print(x,"is a leap year.")
            
else:
            print(x,"is not a leap year.")