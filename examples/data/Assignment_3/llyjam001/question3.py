message=input("Enter the message:\n")
repeats=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
dash=0
length=len(message)
number=thickness

for i in range(thickness):
    print('|'*dash, '+', '-'*(len(message)+2*(number)),'+', '|'*dash, sep='')
    dash=dash+1
    number=number-1
    
for i in range(repeats):
    print('|'*thickness+" "+message+" "+'|'*thickness)
    
dash=dash-1
number=number+1
for i in range(thickness):
    print('|'*dash, '+', '-'*(len(message)+2*(number)),'+', '|'*dash, sep='')
    dash=dash-1
    number=number+1
    
    
    