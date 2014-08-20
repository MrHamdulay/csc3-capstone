msg = input("Enter the message:\n")
           
count = eval(input("Enter the message repeat count:\n"))

thickness = eval(input("Enter the frame thickness:\n"))

for i in range(1,thickness+1):
    print((i-1)*'|','+','-'*(len(msg)+(thickness+1-i)*2),'+',(i-1)*'|',sep='')

for i in range(1,count+1):
    print('|'*thickness+ ' '+ msg + " " + '|'*thickness)
    
for i in range(thickness,0,-1):
    print((i-1)*'|','+','-'*(len(msg)+(thickness+1-i)*2),'+',(i-1)*'|',sep='')
        