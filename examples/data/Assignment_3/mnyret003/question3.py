message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
for i in range(0,frame):
    print('|'*i,'+','-'*(2*frame-(2*i)+len(message)), '+','|'*i,sep='')
for p in range(0,repeat):
    print('|'*(i+1),' ',message,' ','|'*(i+1),sep='')
for e in range(frame-1,-1,-1):
    print('|'*e,'+','-'*(2*frame-(2*e)+len(message)), '+', '|'*e,sep='')
    