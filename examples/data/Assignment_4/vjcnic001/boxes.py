#Question 1

#Write a Python module that contains the following 3 functions to create hollow boxes of stars.

#print_square (), that prints a 5x5 box on the screen
#print_rectangle (width, height), that prints a box on the screen with given width and height
#get_rectangle (width, height) that returns a string containing a box with given width and height
#A python module is a file containing Python code just like a regular program. Typically such a module will contain only functions. To use the module in another program, we first issue the import statement, then refer to each function by prefixing it with the module name.

#Sample I/O:

#Choose test:
#a
#*****
#*   *
#*   *
#*   *
#*****
#Sample I/O:

#Choose test:
#b 3 4
#calling function
#***
#* *
#* *
#***
#called function
#Sample I/O:

#Choose test:
#c 4 3
#calling function
#called function
#****
#*  *
#****
#Save your module as boxes.py. The main program has been supplied as question1.py - use this to test your program and do not change this file.

def print_square():
	print("*****\n*   *\n*   *\n*   *\n*****")
	
def print_rectangle(width,height):
	print("*"*width)
	for i in range(height-2):
		print("*"+" "*(width-2)+"*")
	print("*"*width)

def get_rectangle(width,height):
	return("*"*width+"\n"+("*"+" "*(width-2)+"*\n")*(height-2)+"*"*width)
	
