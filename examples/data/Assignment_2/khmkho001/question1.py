leaps=eval(input("Enter a year:\n"))
if(leaps%400==0 or leaps%4==0 and leaps%100!=0):
    print(leaps,"is a leap year.")
else:print(leaps,"is not a leap year.")