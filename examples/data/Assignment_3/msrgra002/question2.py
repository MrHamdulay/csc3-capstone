#Grant Meeser
#MSRGRA002
#25/03/2014

w=' '
s='*'
n=eval(input('Enter the height of the triangle:\n'))

for i in range(n):
	print((w*((n-1)-i))+s+(s*(i*2))+(w*((n-1)-i)))


