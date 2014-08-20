def messagePrint(number, message, thickness):
	boarder = thickness*"|"
	for i in range(number):
		print(boarder + " " + message + " " + boarder )

def boarder(length, thickness, placement):
	bar = "-" * (length + 2)
	if placement == "TOP":		
		for i in range(0, thickness):
			left = "|"*i + "+" + "-"*(thickness - 1 - i)
			right = left[::-1]
			print(left + bar + right)
	elif placement == "BOTTOM":
		for i in range(thickness-1, -1, -1):
			left = "|"*i + "+" + "-"*(thickness - 1 - i)
			right = left[::-1]
			print(left + bar + right)
def main():
	message = input("Enter the message:\n")
	count = eval(input("Enter the message repeat count:\n"))
	thickness = eval(input("Enter the frame thickness:\n"))
	messageLength = len(message)
	boarder(messageLength, thickness, "TOP")
	messagePrint(count, message, thickness)
	boarder(messageLength, thickness, "BOTTOM")
	
main()	

'''
Enter the message:
Hello World
Enter the message repeat count:
3
Enter the frame thickness:
2
+---------------+
|+-------------+|
|| Hello World ||
|| Hello World ||
|| Hello World ||
|+-------------+|
+---------------+
'''
