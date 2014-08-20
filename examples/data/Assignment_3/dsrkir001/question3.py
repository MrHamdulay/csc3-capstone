message = (input("Enter the message:\n"))
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
smessage = (len(message)+2)
x=(smessage+((thickness-1)*2))
y = 0
a = thickness
d = thickness-1
while thickness > 0:
    print('|'*y,'+','-'*x,'+','|'*y,sep='')
    x=x-2
    y=y+1
    z=thickness-1
    thickness=thickness-1
  
while repeat > 0:
    print('|'*a,' ',message,' ','|'*a,sep='')
    repeat=repeat-1

c = (len(message)+2)
x=x+2
while  d > -1:
    
    print('|'*d,'+','-'*x,'+','|'*d,sep='')
    x=x+2
    y=y-1
    repeat=repeat+1
    d=d-1
    