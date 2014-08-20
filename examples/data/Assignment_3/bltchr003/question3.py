message = " "+input("Enter the message:\n")+" "
repeat = eval(input("Enter the message repeat count:\n"))
framethick = eval(input("Enter the frame thickness:\n"))

for i in range(framethick):
    print(i * "|", "+", (len(message)+(framethick-1)*2-(2*i))*"-" , "+", i * "|", sep="")
    

for i in range(repeat):
    print("|"*framethick,message,"|"*framethick, sep="")
    
for i in range(framethick-1,-1,-1):
    print(i * "|","+", (len(message)+(framethick-1)*2-(2*i))*"-", "+",i * "|",sep="")