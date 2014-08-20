a = eval(input("Enter a year:\n"))


if a/400==a//400:
     print(a,"is a leap year.")
     
elif a/4==a//4 and not a/100==a//100:
     print(a,"is a leap year.")
     
else:
     print(a,"is not a leap year.")
     


