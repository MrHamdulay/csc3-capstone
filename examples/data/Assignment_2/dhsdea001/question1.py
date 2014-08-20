#Question 1
#By: Dean de Haast

def isleapyear(x):
    if x%400 == 0:
        x=str(x)
        print(x +" is a leap year.")
    elif x%4 == 0 and x%100!=0:
        x=str(x)
        print(x +" is a leap year.")
    else:
        x=str(x)
        print( x + " is not a leap year.")     
     
    
year= eval(input("Enter a year:""\n"))
isleapyear(year)