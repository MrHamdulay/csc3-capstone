import math

val = 8

def printFunction(function):
	row = ""
	for i in range(10, -11,-1):
		for x in range(-10, 11):
			if getValue(function, x) == i:
				row += "o"
			elif x == 0 and i == 0:
				row += "+"
			elif x == 0:
				row += "|"
			elif i == 0:
				row += "-"
			else:
				row += " "
		row += "\n"
	return row

def getValue(function, x):
	function.replace("x", str(x))
	#print(function)
	val = eval(function)
	#print(val)
	return round(val)
	
function = input("Enter a function f(x):\n")
print(printFunction(function))



"""
Write a program to draw a text-based graph of a mathematical function f(x).

Use axis limits of -10 to 10, with only discrete points plotted. Use nested loops to scan through the entire area of the graph and wherever the (rounded) value of f(x) is equal to the y, output "o" (small letter Oh). Otherwise, output either the appropriate axis character or a space. Remember to import math to use some mathematical functions.

To support entering of arbitrary functions, the user must enter a string at first. The Python eval function must then be invoked each time to compute the function value for different values of x.

Sample I/O:

Enter a function f(x):
x+2
          |       o  
          |      o   
          |     o    
          |    o     
          |   o      
          |  o       
          | o        
          |o         
          o          
         o|          
--------o-+----------  NOTE: -10 to 10
       o  |          
      o   |          
     o    |          
    o     |          
   o      |          
  o       |          
 o        |          
o         |          
          |          
          |          

Save your program as question4.py.
"""
