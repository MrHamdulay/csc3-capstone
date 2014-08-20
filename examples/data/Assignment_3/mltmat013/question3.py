message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
counter = thickness*2  
for i in range(thickness):
        print('|'*i + '+' + '-'*(len(message)+ counter) +'+' + '|'*i)
        counter -= 2
for i in range(repeat):
        print('|'*thickness + ' ' + message + ' ' + '|'*thickness)
counter = 2
for i in range(thickness-1,-1,-1):
        print('|'*i + '+' + '-'*(len(message)+ counter) +'+' + '|'*i)
        counter += 2
