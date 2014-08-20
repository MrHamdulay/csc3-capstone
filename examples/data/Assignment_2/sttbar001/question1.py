year = eval(input("Enter a year: \n"))
new = int(year/400)
ne = int(year/4)
n = int(year/100)
if(year==new*400 or (year==ne*4 and year!=n*100)):
    print(str(year)+" is a leap year.")
else:
    print(str(year)+" is not a leap year.")