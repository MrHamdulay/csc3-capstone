height = eval(input("Enter the height of the triangle:\n"))
j = 1
for n in range(1,height+1):
	space = height-n
	if n == 1:
		print(space*" "+j*"*")
	else:
		j = j+2
		print(space*" "+j*"*")
	
	
	
	