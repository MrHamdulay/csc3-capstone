x= eval(input("Enter a year:\n"))
yr1=x//4
yr2=x/4
yr3=round(yr2-yr1,100)
yr4 = x/400
yr5 = x//400
if yr4== yr5:
        print(x,"is a leap year.")
else:
        if yr3==0:
                if (yr2//100)==(round(yr1/100,1000)):
                        print(x,"is not a leap year.")
                else:
                        print(x,"is a leap year.")
        else:
                print(x,"is not a leap year.")

