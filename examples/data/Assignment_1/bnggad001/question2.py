#question 2

def time():  #define function

	if (0<=a<=23) and (0<=b<=59) and (0<=c<=59):  #checks all the parameters are met
	
		print("Your time is valid.")
		
	else:
		print("Your time is invalid.")
			
a = int(input("Enter the hours:\n"))
b = int(input("Enter the minutes:\n"))
c = int(input("Enter the seconds:\n"))

time()
