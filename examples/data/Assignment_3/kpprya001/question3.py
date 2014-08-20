message=(input ("Enter the message:\n"))
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
frame2 = frame

space2=repeat
lines2 = len(message)+2

for i in range (frame):
    print("|"*i,"+","-"*(len(message)+(2*frame)),"+","|"*i,sep="")
    frame -=1

frame = frame2

for i in range (repeat):
    print("|"*frame2,message,"|"*frame2,)
    

for i in range (frame2):
    print("|"*(frame-1),"+","-"*(lines2),"+","|"*(frame-1),sep="")
    frame-=1
    lines2+=2    
    
