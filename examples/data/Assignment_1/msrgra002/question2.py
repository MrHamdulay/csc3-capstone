#Time
#Grant Meeser MSRGRA002
#26/2/2014

#Get integerset
hour = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
#create valid boolean
valid=False

if 0<=hour<=23 and 0<=minutes<=59 and 0<=seconds<=59:
	print("Your time is valid.")
else:
	print("Your time is invalid.")


