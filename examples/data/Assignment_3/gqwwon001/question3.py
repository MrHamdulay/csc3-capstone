print('Enter the message:')
m=input()
print('Enter the message repeat count:')
r=eval(input())
print('Enter the frame thickness:')
t=eval(input())
l=len(m)
#gap=(l+2)*t//t

f = (l*2 + t*2)

for i in range(0,t):
    
    print("|"*i +'+'+'-'*(f-(i+1)*2-l+2)+'+' + "|"*i)
    
for j in range(r):
    print('|'*t ,m, '|'*t)
for i in reversed(range(0,t)):
    print("|"*i +'+'+'-'*(f-(i+1)*2-l+2)+'+' + "|"*i)
    
