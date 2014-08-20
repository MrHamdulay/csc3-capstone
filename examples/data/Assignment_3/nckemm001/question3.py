def frame():
    message = input("Enter the message:\n")
    count = eval(input("Enter the message repeat count:\n"))
    thickness = eval(input("Enter the frame thickness:\n"))
    a = thickness-1
    b = 0
    frame1 = len(message) +(thickness*2)   
    frame2 = len(message)+2
    for b in range(thickness):
        print("|"*b,"+","-"*frame1,"+","|"*b,end="\n",sep="")
        b+=1
        frame1-=2
    for i in range(count):
        print("|"*thickness,message,"|"*thickness)
    for b in range(thickness):
        print("|"*a,"+","-"*frame2,"+","|"*a,end="\n",sep="")
        a-=1
        frame2 +=2
frame()        
        