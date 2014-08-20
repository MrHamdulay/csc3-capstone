import math
x=eval(input("Enter a year:\n"))
if (x/400.0==x//400):
    print(x,"is a leap year.")
elif(x/4.0==x//4) and ((x/100==x//100)==False):
    print(x,"is a leap year.")
else:
    print(x,"is not a leap year.")
