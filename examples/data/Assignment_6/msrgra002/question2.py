#Grant Meeser
#MSRGRA002
#24/04/2014
import math

va = input('Enter vector A:\n').split(' ')
vb = input('Enter vector B:\n').split(' ')

vab=[]
x=0

for i in range(len(va)):
	vab.append(int(va[i])+int(vb[i]))
print('A+B =',vab)


for i in range(len(va)):
	x+=(int(va[i])*int(vb[i]))
print('A.B = '+str(x))

x=0
for i in range(len(va)):
	x+=(math.pow(int(va[i]),2))
print('|A| = '+'{:0.2f}'.format(round(math.sqrt(x),2)))

x=0
for i in range(len(vb)):
	x+=(math.pow(int(vb[i]),2))
print('|B| = '+'{:0.2f}'.format(round(math.sqrt(x),2)))
