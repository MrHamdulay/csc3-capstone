# Bulletin Board System.
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011

import sys

def main():
	print("Welcome to UCT BBS")
	print("MENU\n (E)nter a message\n (V)iew message\n " + \
			"(D)isplay file\n e(X)it")
	sel = input("Enter your selection:\n")

	if sel == "E" or "e":
		mes1 = input("Enter the message:\n")
		print("Welcome to UCT BBS")
		print("MENU\n (E)nter a message\n (V)iew message\n " + \
				"(D)isplay file\n e(X)it")
		sel2 = input("Enter your selection:\n")
		
		if sel2 == "V" or "v":
			print("The message is: ", mes1)
			break
	elif sel == "V" or "v":
		print("no message yet")
	elif sel == "L" or "l":
		print("List of files: 42.txt, 1015.txt")
	elif sel == "D" or "d":
		name = input("Enter the filename:\n")
	elif sel == "X" or "x":
		print("Goodbye!")
		sys.exit()
		
# Call function main.
main()