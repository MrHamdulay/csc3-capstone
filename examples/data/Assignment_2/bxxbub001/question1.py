#B.Booi
#13 march 2014
#tell if a leapyear

def leapyear():
    year = eval(input("Enter a year:\n"))
    if year % 400 == 0:
        print(year,"is a leap year.")
    elif year % 4 ==0 and year %100 != 0:
        print(year,"is a leap year.")
    else:
        print(year, "is not a leap year.")
        

leapyear()
  