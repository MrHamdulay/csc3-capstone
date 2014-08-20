message = input("Enter the message:\n")
repeat  = eval(input("Enter the message repeat count:\n"))
thick   = eval(input("Enter the frame thickness:\n"))
    
t= (len(message)+2*thick)
for i in range(thick):
       print("|"*i,"+","-"*t,"+","|"*i,sep='')
       t-=2
    
for j in range(repeat):
       print("|"*thick," ", message, " " , "|"*thick, sep='')
    
y= len(message)+2
x=thick-1
    
for k in range(thick):
       print("|"*x,"+","-"*y,"+", "|"*x,sep='')
       y+=2
       x-=1