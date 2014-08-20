text=input('Enter the message:\n')
repeat=eval(input('Enter the message repeat count:\n'))
thickness=eval(input('Enter the frame thickness:\n'))
a=len(text)+2*thickness
b=0
for i in range(thickness):
    print('|'*b+'+'+a*'-'+'+'+'|'*b)
    a-=2
    b+=1
c=b
for i in range(repeat):
    print('|'*c+' '+text+' '+'|'*c)
f=thickness-1
e=len(text)+2
for i in range(thickness):
    print('|'*f+'+'+e*'-'+'+'+'|'*f)
    e+=2
    f-=1