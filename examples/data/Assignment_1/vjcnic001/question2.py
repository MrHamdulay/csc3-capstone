hours = eval(input("Enter the hours:\n"))
minute = eval(input("Enter the minutes:\n"))
second = eval(input("Enter the seconds:\n"))
if(0<=(hours)<=23) and (0<=(minute)<=59) and (0<=(second)<=59):
	print("Your time is valid.")
else:
	print("Your time is invalid.")
	