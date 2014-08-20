paid = 0
costCents = eval(input("Enter the cost (in cents):\n"))




def changeGet(value):
	global change
	changePre = change//value
	change = change%value
	#print("get change working...", change, changePre)
	return changePre
	
def printChange(amount, postFix):
	if amount != 0:
		print(amount, postFix)


while paid < costCents:
	 paid += eval(input("Deposit a coin or note (in cents):\n"))

change = paid - costCents
changeDolars = changeGet(100)
change25 = changeGet(25)
change10 = changeGet(10)
change5 = changeGet(5)

if paid != costCents:
	print("Your change is:")
	printChange(changeDolars, "x $1")
	printChange(change25, "x 25c")
	printChange(change10, "x 10c")
	printChange(change5, "x 5c")
	printChange(change, "x 1c")


"""
Assume that all change is given in coins only and coins come in the following denominations: 1c, 5c, 10c, 25c, $1

Sample I/O:

Enter the cost (in cents):
750
Deposit a coin or note (in cents):
500
Deposit a coin or note (in cents):
500
Your change is:
2 x $1
2 x 25c
"""
