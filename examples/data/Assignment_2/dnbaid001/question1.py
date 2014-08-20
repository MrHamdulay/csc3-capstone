year = eval(input("Enter a year:\n"))
if year%400 ==0 or (year%4 == 0 and year%100 !=0): #year inputted must be divisible by 400 OR it must be divisible by 4 but not by 100 to account for time lost every 100 years.
    print (year, "is a leap year.")
else:
    print (year, "is not a leap year.")