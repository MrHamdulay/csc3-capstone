import math
def main():
	function = input("Enter a function f(x):\n")
	for y in range (10,-11,-1):
		for x in range(-10,11):
			sinx = math.sin(x)
			tanx = math.tan(x)
			cosx = math.cos(x)
			if round(eval(function)) ==y:
				print("o", end = "")
			elif y == 0 and x == 0:
				print("+",end = "")
			elif x == 0:
				print("|", end = "")
			elif y == 0:
				print("-", end = "")
			else:
				print(" ",end="")
		print()
main()