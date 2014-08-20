def leapyear(x):
    if  x%4==0 and x%100!=0 or x%400==0:
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")
        
x=eval(input("Enter a year:\n"))        
leapyear(x)
