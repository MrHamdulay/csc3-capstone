h = int(input("Enter the hours:\n"))
m = int(input("Enter the minutes:\n"))
s = int(input("Enter the seconds:\n"))
if (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
	print("Your time is valid.")
else:
	print("Your time is invalid.")

