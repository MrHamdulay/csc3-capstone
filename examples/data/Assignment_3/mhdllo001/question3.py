x=input('Enter the message:\n')
y=eval(input('Enter the message repeat count:\n'))
z=eval(input('Enter the frame thickness:\n'))
for i in range(z):
        print('|'*(i) + '+' + '-'*(len(x) ) + '-'*(2*z-2*i) + '+' + '|'*(i))
        
for i in range(y):
        print(('|'*z)+ ' ' + x + ' ' + ('|'*z))

for i in range(z):
        print('|'*(z-i-1) + '+' + '-'*(len(x)) + '-'*(2*i+2)  + '+' + '|'*(z-i-1))