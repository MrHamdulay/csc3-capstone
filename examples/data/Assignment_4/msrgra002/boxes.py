#MSRGRA002
#Grant Meeser
#03/04/2014

def get_rectangle(w,h):
	s=('*'*w)+'\n'
	s+=('*'+(' ')*(w-2)+'*\n')*(h-2)
	s+=('*'*w)
	return s

def print_rectangle(w,h):
	print(get_rectangle(w,h))

def print_square():
	print(get_rectangle(5,5))


