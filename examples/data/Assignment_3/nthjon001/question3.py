message=input("Enter the message:\n")
repeat_count=eval(input("Enter the message repeat count:\n"))
frame_thick=eval(input("Enter the frame thickness:\n"))
for i in range(0,frame_thick):
    print('|'*i, '+', '-'*(2*frame_thick-(2*i)+len(message)), '+', '|'*i,sep='')
for p in range(0,repeat_count):
    print('|'*(i+1),' ',message,' ','|'*(i+1), sep='')
for e in range(frame_thick-1,-1,-1):
    print('|'*e, '+', '-'*(2*frame_thick-(2*e)+len(message)), '+', '|'*e,sep='')