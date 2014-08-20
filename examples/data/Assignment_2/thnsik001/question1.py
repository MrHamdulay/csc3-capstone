#question 1 assignment 2


year = eval(input("Enter a year:\n"))
leap = False
if(type(year) == int):
    if(year%400==0):
        leap = True
    elif((year%4==0) and (year%100!=0)):
        leap = True

    if(leap == False):
        print(year,"is not a leap year.")
    if(leap == True):
        print(year,"is a leap year.")
else:
    print("not a year")
    