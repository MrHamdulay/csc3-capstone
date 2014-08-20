answer=eval(input("Enter a year:\n"))
if answer%400==0:
    print(answer, "is a leap year.")
elif answer%4==0 and answer%100!=0:
    print(answer, "is a leap year.")
else:
    print(answer, "is not a leap year.")
    
