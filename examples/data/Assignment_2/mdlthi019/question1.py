year = eval(input("Enter a year:\n"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year.")
        else:
            print(year,"is not a leap year.")
    else:
        print(year,"is a leap year.")
#if number entered that is not part of the restrictions 
else:
    print(year,"is not a leap year.")
    
   