word=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
x=0
z=len(word)+thickness*2
y=thickness-1
w=len(word)+2

for i in range(thickness):
    print('|'*x, '+', '-'*z, '+', '|'*x, sep='')
    x+=1
    z=z-2
for j in range(repeat):
    print("|"*thickness,word,'|'*thickness)
    
    
for i in range(thickness):
    print('|'*y, '+', '-'*w, '+', '|'*y, sep='')
    y=y-1
    w+=2