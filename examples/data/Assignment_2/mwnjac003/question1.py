# leap year
def leap_year():
    x=eval(input("Enter a year:\n"))
    if (x%400==0) or (x%100!=0 and x%4==0):
        print(x,"is a leap year.")
    else: print(x,"is not a leap year.")
leap_year()
