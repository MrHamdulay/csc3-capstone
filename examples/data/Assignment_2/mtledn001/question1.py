year = eval(input("Enter a year:\n"))
if((year%400==0)):
    print(year,"is a leap year.")
    # it is divisible by 4 but not by 100.
elif(year%4==0 and not year%100==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")