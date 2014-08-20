t= eval(input("Enter a year:\n"))
if(t%400==0 or t%4==0 and t%100!=0):
    print(t,"is a leap year.")
else:
    print(t,"is not a leap year.")