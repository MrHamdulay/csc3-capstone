year=eval(input("Enter a year:\n"))
remainder= year % 400 #testing for division by 400
if remainder==0:
    print(year,"is a leap year.")
else:
    remainder= year % 4 #testing for division by 4
    remainder2= year % 100 #testing for division by 100
    if (remainder==0) and (remainder2>0):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
        
   
    