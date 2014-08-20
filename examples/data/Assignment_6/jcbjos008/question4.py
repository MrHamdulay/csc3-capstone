'''Joshen Credelio Jacob
histogram of marks
21/04/2014'''
x=input('Enter a space-separated list of marks:\n')
x=x.split()

f=0
su=0
sl=0
t=0
F=0

#calculating each group
for i in range(len(x)):
    y=eval(x[i])
    if y>=75:
        f+=1
    elif y>=70:
        su+=1
    elif y>=60:
        sl+=1
    elif y>=50:
        t+=1
    else:
        F+=1
        
#printing histogram
print('1 |'+'X'*f)
print('2+|'+'X'*su)
print('2-|'+'X'*sl)
print('3 |'+'X'*t)
print('F |'+'X'*F)