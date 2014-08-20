mes = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
def dash():
	size_dash =(len(mes)+2*frame)
	b = 0
	for a in range(frame):
		print(b*'|'+'+'+"-"*size_dash+'+'+b*'|')
		size_dash = (size_dash)-2
		b=b+1

def string():
	for s in range(count):
		print('|'*frame+" "+mes+" "+'|'*frame)
		
#+---------------+
#|+-------------+|
#|| Hello World ||
#|| Hello World ||
#|| Hello World ||
#|+-------------+|
#+---------------+
def bottom():
	hi = frame -1 
	size_dash = len(mes)+2
	for a in range(frame):
		print(hi*'|'+"+"+size_dash*"-"+"+"+"|"*hi)
		hi = hi -1
		size_dash = size_dash+2


dash()		
string()
bottom()