import math
q=input('Enter vector A:\n')
w=input('Enter vector B:\n')
e=q.replace(' ',',')
r=w.replace(' ',',')
t=e.split(',')
y=r.split(',')


u=str(eval(t[0])+eval(y[0]))
i=str(eval(t[1])+eval(y[1]))
o=str(eval(t[2])+eval(y[2]))
print('A+B = ['+u+', '+i+', '+o+']')

p=eval(t[0])*eval(y[0])
a=eval(t[1])*eval(y[1])
s=eval(t[2])*eval(y[2])
d=str(p+a+s)
print('A.B = '+d)

f=eval(t[0])**2
g=eval(t[1])**2
h=eval(t[2])**2
j=math.sqrt(f+g+h)
k=str(round(j,2))
if k=='0.0':
   print('|A| = '+k+'0')
else:
   print('|A| = '+k)

   
l=eval(y[0])**2
z=eval(y[1])**2
x=eval(y[2])**2
c=math.sqrt(l+z+x)
v=str(round(c,2))
if v=='0.0':
   print('|B| = '+v+'0')
else:
   print('|B| = '+v)