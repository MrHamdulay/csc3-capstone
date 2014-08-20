# 1c, 5c, 10c, 25c, $1

# Sample I/O:

# Enter the cost (in cents):
# 750
# Deposit a coin or note (in cents):
# 500
# Deposit a coin or note (in cents):
# 500
# Your change is:
# 2 x $1
# 2 x 25c
# Save your program as question2.py.

total = 0
cost = eval(input("Enter the cost (in cents):\n"))
while cost > total:
	deposit = eval(input("Deposit a coin or note (in cents):\n"))
	total = total + deposit
change = total - cost
while change>0:
	print("Your change is:")
	ones = change//100 
	if ones != 0:
		print(ones, "x $1")
	change = change - (ones*100)
	quarters = change//25
	if quarters != 0:
		print(quarters, "x 25c")
	change = change - (25*quarters)
	tens = change//10 
	if tens != 0:
		print(tens, "x 10c") 
	change = change - (tens*10)
	five = change//5
	if five != 0:
		print(five, "x 5c")
	change = change - (5*five) 
	if change != 0:
		print(change, "x 1c")
	break
