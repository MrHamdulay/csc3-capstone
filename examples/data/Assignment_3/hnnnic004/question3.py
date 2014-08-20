message=input("Enter the message:\n")
rep=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
length=len(message)+2*frame

#top: i-1*1 + -*(len(message)+2) +*i
i=1
while i<=frame:
   
    print("|"*(i-1), end="")
    print("+", end="")
    print("-"*length, end="")
    print("+", end="")
    print("|"*(i-1))
    
    i+=1
    length-=2

#body:
i=1
while i<=rep:
    print("|"*frame, message, "|"*frame)
    i+=1

#end:
i=frame
while i>=1:
    print("|"*(i-1), end="")
    print("+", end="")
    print("-"*(length+2), end="")
    print("+", end="")
    print("|"*(i-1))
       
    i-=1
    length+=2