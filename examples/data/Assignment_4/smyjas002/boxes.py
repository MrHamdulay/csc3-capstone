def print_square ():
	print("""*****
*   *
*   *
*   *
*****
""")


def print_rectangle (width, height):
	print("*"*width)
	for i in range(height-2):
		print('*','*',sep=" "*(width-2))
	print("*"*width)

def get_rectangle (width, height):
	string = "*"*width + '\n'
	for i in range(height-2):
		string += '*' + " "*(width-2) + '*'+ '\n'
	string += "*"*width 
	return string


"""

    print_square (), that prints a 5x5 box on the screen
    print_rectangle (width, height), that prints a box on the screen with given width and height
    get_rectangle (width, height) that returns a string containing a box with given width and height

**************
**************

Choose test:
a
*****
*   *
*   *
*   *
*****

Sample I/O:

Choose test:
b 3 4
calling function
***
* *
* *
***
called function

Sample I/O:

Choose test:
c 4 3
calling function
called function
****
*  *
****

"""
