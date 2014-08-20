#QUESTION 1.1
year=eval(input("Enter a year:\n"))
if year%400==0:
    print(year,"is a leap year.\n")
else: 
    if (year%4==0)&(year%100!=0):
        #&(year%100!=0):
        print(year,"is a leap year.\n")
    else:
        print(year,"is not a leap year.\n")


    


