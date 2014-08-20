def leapyear(v):    
    if v%400==0:
        print(v,"is a leap year.")
    elif v%4==0 and v%100!=0:
        print(v,"is a leap year.")
    else:
        print(v,"is not a leap year.")
        
v = eval(input("Enter a year:\n"))  

leapyear(v)