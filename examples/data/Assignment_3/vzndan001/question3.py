x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))

lmsg=len(x)
lmsg2=lmsg+(z*2)



for top in range(z):
    print("|"*(top),"+","-"*lmsg2 ,"+","|"*(top),sep='')
    lmsg2=lmsg2-2
for i in range(y):
    print(z*'|',x,'|'*z) 
for bottom in range(z,0,-1):    
    print("|"*(bottom-1),"+","-"*lmsg2,2*"-" ,"+","|"*(bottom-1),sep='')
    lmsg2=lmsg2+2
