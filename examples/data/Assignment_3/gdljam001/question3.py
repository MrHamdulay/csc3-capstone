#Enter the message:
#Hello World
#Enter the message repeat count:
#3
#Enter the frame thickness:
#2
#+---------------+
#|+-------------+|
#|| Hello World ||
#|| Hello World ||
#|| Hello World ||
#|+-------------+|
#+---------------+


message=input("Enter the message:\n");
repeat= eval(input("Enter the message repeat count:\n"));
frame= eval(input("Enter the frame thickness:\n"));
for x in range (frame):
    print(("|"*x),end="");
    print ("+",end="");
   
    print("-"*(len(message)+(frame-x)*2),end="");
    print("+",end="");
    print(("|"*x));

rep= (("|"*(frame))+" "+message+" "+("|"*(frame)))
for y in range (repeat):
    print(rep)
    
for j in range (frame):
    print(("|"*(frame-j-1)),end="")
    print("+",end="")
    print("-"*(len(message)+(j+1)*2),end="");
    print ("+",end="");
    print(("|"*(frame-j-1)));
    
    
    