#Grant Meeser
#MSRGRA002
#13/02/2014
import math


def pi():
	s = 2
	t = 0
	a = 0
	i=0
	while t!=1:
		for x in range(0,i+1):
			a= math.sqrt(2+a)
			#print(str(a))
		t=2/a
		s=s*t
	return s
	


print('Approximation of pi: '+str(round(pi(),3)))
r=eval(input('Enter the radius:\n'))
area = r*r*pi()
print('Area:',str(round(area,3)))
