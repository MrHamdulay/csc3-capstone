# Message with dynamic bordering

message = input('Enter the message: ''\n')
repeat = eval(input('Enter the message repeat count: ''\n'))
thick = eval(input('Enter the frame thickness: ''\n'))
length = len(message)


for i in range(0,thick):
    print('|'*i, '+', '-'*(length - 2*i + 2*thick), '+', '|'*i, sep='')
    
for i in range(repeat):
    print('|'*thick, message, '|'*thick)
    
for i in range (thick-1,0-1,-1):
    print('|'*i, '+', '-'*(length - 2*i + 2*thick), '+', '|'*i, sep='')
    
    

    

