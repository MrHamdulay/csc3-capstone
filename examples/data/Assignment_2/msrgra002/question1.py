#Grant Meeser
#MSRGRA002
#13/02/2014

year = eval(input("Enter a year:\n"))

if((year % 400)==0)  or ((year % 100)!=0 and (year % 4)==0):
	print(str(year)+" is a leap year.")
else:
	print(str(year)+" is not a leap year.")
