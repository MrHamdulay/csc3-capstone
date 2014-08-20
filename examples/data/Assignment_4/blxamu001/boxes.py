

def print_square(): # function that prints a 5*5, box
	print('*****')
	print('{0}{1:>4}'.format('*','*'))
	print('{0}{1:>4}'.format('*','*'))
	print('{0}{1:>4}'.format('*','*'))
	print('*****')

def print_rectangle(width,height): # Function that draws box given width and height
	line = ('*'+' '*(width-2)+'*\n')
	height = line*(height-2)
	rectangle = ('*'*width+'\n'+height+'*'*width)
	print(rectangle)

def get_rectangle(width,height): # Function that returns a string of a box
	
	line = ('*'+' '*(width-2)+'*\n')
	height = line*(height-2)
	rectangle = ('*'*width+'\n'+height+'*'*width)
	return(rectangle)
