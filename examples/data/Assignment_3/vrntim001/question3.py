message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
i = 0
x = 0
a = (len(message)+2*frame)
while x < frame:
        print("|"*x,"+","-"*a,"+","|"*x, sep="")
        x+=1
        a-=2
while i < repeat:
        print("|"*frame," ",message," ","|"*frame,sep="")
        i+=1        
while x != 0:
        x-=1
        a+=2  
        print("|"*x,"+","-"*a,"+","|"*x, sep="")
          
