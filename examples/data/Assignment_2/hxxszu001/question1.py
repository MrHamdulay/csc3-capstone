x=eval(input("Enter a year: \n"))
if x%400==0:
    print( x,"is a leap year.\n")
elif x%4==0 and x%100!=0:
    print( x,"is a leap year.\n")
else:
    print( x,"is not a leap year.\n")
    
