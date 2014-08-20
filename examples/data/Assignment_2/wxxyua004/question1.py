#question1
def leapyear(x):    
    if x%4==0 and x!=2100:
        print(x,"is a leap year.")
    elif x%4!=0 or x==2100:
        print(x,"is not a leap year.")
        
x=eval(input("Enter a year:\n"))        
leapyear(x)