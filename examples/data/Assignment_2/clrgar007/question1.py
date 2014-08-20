leap=eval(input("Enter a year:\n"))
if   leap%4==0 and leap%100!=0:
        print(leap,"is a leap year.")
elif leap%400==0:
        print(leap,"is a leap year.")

else:
        print(leap,"is not a leap year.")
        

    