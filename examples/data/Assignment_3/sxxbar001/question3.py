#Assignment 3
#Question 3
#25 March 2014
#Program to draw a frame surrounding a message

msg=input("Enter the message: \n")
rpt=eval(input("Enter the message repeat count: \n"))
frame=eval(input("Enter the frame thickness: \n"))

for i in range(frame):
    print('|'*i,'+',"-"*(len(msg)+2*frame-2*i),'+','|'*i,sep="")

for j in range(rpt):
    print('|'*frame,msg,'|'*frame)

for k in range(frame,0,-1):
    k=k-1
    print('|'*k,'+',"-"*(len(msg)+2*frame-2*k),'+','|'*k,sep="")