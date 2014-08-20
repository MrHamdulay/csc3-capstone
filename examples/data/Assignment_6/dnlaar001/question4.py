s=input('Enter a space-separated list of marks:\n')
r=s.replace(' ',',')
q=r.split(',')
e=0
d=0
c=0
b=0
a=0
for i in range(len(q)):
    u=eval(q[i])
    if u<50:
        e+=1
    elif 50<=u<60:
        d+=1
    elif 60<=u<70:
        c+=1
    elif 70<=u<75:
        b+=1
    elif u>=75:
        a+=1
print('1 |'+a*'X')
print('2+|'+b*'X')
print('2-|'+c*'X')
print('3 |'+d*'X')
print('F |'+e*'X')
    