#------------------------------------------------------------
# A Python module that contains the following 
# 3 functions to create hollow boxes of stars.
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011
#------------------------------------------------------------

def print_square():
	print("*" * 5)
	space = "   "
	for j in range(3):
		print("*"+ space +"*")
	print("*" * 5)

def print_rectangle(width, height):
	print("*" * width)
	spa = " " * (width - 2)
	for i in range(height):
		print("*" + spa + "*")
	print("*" * width)

def get_rectangle(width, height):
	print("calling function \ncalled function")
	print("*" * width)
	sp = " " * (width - 2)
	for i in range(height):
		print("*" + sp + "*")
	print("*" * width)