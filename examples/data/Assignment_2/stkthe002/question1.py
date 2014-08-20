 #A year is a leap year if 
 #(a) it is divisible by 400 or (b) it is divisible by 4 but not by 100.
 
 #Enter a year:
 #2008
 #2008 is a leap year.
 
year = eval(input("Enter a year: \n"))
 
if (not year%400 or (not year%4 and year%100)):
 print(year, "is a leap year.")
else:
 print(year, "is not a leap year.")
                
                   