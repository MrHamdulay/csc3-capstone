def leap_year():
    year=eval(input("Enter a year:\n"))
    if year%x==0 or (year%y==0 and year%z!=0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
    
x,y,z=400,4,100

leap_year()