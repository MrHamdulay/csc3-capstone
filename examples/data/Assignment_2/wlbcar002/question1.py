year = eval(input("Enter a year:\n"))

if((year%400 == 0) or (year%4 ==0 and not (year%100==0))):
    #print(year%400)
    print(str(year)+" is a leap year.")
else:
    print(str(year)+" is not a leap year.")
    