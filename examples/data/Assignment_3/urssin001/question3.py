#Write a program to draw a frame (made of the characters +-|) around a message
#that has been repeated on consecutive lines.  
#There is a space before and after the message, and no spaces between concentric boxes.
m=input("Enter the message:\n")
repeatm=eval(input("Enter the message repeat count:\n"))
fthickness=eval(input("Enter the frame thickness:\n"))
k=len(m)+(fthickness*2)
L=(repeatm+fthickness*2)
frame ="+"+"-"*k+"+"
z=fthickness-1
if fthickness==1:
        print("+","-"*k,sep="",end="+\n")
        print("|"*fthickness,m,"|"*fthickness)   
        print("+","-"*k,sep="",end="+\n")
for i in range(L):
        if fthickness==1: break
        else:
            if i in range(0,fthickness-1):
                if i==0:print("+","-"*k,sep="",end="+\n")
                if fthickness>1:
                    print("|"*(i+1),"+","-"*(k-2),"+","|"*(i+1),sep="",end="\n")
                    k-=2
            elif i in range(fthickness,L-fthickness):
                print("|"*fthickness,m,"|"*fthickness)    
                    
            elif i in range(fthickness+repeatm,L-1):
                if fthickness>1:
                    print("|"*(z),"+","-"*(k),"+","|"*(z),sep="",end="\n")
                    z-=1
                    k+=2 
            if i==L-1:print("+","-"*(k),sep="",end="+\n")
                