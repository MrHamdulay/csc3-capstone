def leap():
    x=eval(input("Enter a year:\n"))
    calc1= x%400
    calc2=x%4
    if calc1==0:
        print(x,"is a leap year.")
    elif calc2==0 and x%100!=0:
        print(x,"is a leap year.")
    else: 
        print(x,"is not a leap year.")
    
leap()
    
