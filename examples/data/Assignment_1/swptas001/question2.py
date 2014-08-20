#Time Checking
#Tashiv Sewpersad
#25-02-2014

iHour = eval(input("Enter the hours:"+"\n"))
iMinute = eval(input("Enter the minutes:"+"\n"))
iSecond = eval(input("Enter the seconds:"+"\n"))

if (iHour >= 0) and (iHour <= 23) and (iMinute >= 0) and (iMinute <= 59) and (iSecond >= 0) and (iSecond <= 59):
	print("Your time is valid.")
else:
	print("Your time is invalid.")