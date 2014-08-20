import math
def year():
    x=eval(input("Enter a year:\n"))
    y=(x/400)
    z=(x/4)
    n=(x//400)
    g=(x//4)
    r=(x%100)
    if  (y==n or z==g and r!=0):
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")
year()