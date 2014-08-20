#MDLKUR001

def print_square(): 
	print('*****')
	print('{0}{1:>4}'.format('*','*'))
	print('{0}{1:>4}'.format('*','*'))
	print('{0}{1:>4}'.format('*','*'))
	print('*****')

def print_rectangle(w,h): 
	newline = ('*'+' '*(w-2)+'*\n')
	h = newline*(h-2)
	r = ('*'*w+'\n'+h+'*'*w)
	print(r)

def get_rectangle(w,h): 
	
	newline = ('*'+' '*(w-2)+'*\n')
	h = newline*(h-2)
	r= ('*'*w+'\n'+h+'*'*w)
	return(r)
