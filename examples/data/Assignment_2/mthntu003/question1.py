x= eval(input("Enter a year:\n"))
x1=x//4
x2=x/4
x3=round(x2-x1,100)
x4 = x/400
x5 = x//400
if x4== x5:
        print(x,"is a leap year.")
else:
        if x3==0:
                if (x2//100)==(round(x1/100,1000)):
                        print(x,"is not a leap year.")
                else:
                        print(x,"is a leap year.")
        else:
                print(x,"is not a leap year.")

