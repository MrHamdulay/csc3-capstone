year=eval(input("Enter a year:\n"))

first=year%400
second=year%4
third=year%100

if first==0:
    print(year,"is a leap year.")
elif second==0 and third!=0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")



    