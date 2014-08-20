x=eval(input("Enter a year:\n"))
if x%400==0:
    print(x,"is a leap year.")
elif x%100!=0 and x%4==0:
    print(x, "is a leap year.\n")
else:
    print(x,"is not a leap year.")
            
    

    
        
    