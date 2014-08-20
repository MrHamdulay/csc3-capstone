a = input("Enter the message:\n")
b = eval(input("Enter the message repeat count:\n"))
c = eval(input("Enter the frame thickness:\n"))

length = len(a)
for i in range(c):
    print("|"*(i),"+","-"*(length+2*c-2*i),"+","|"*(i),sep='')
    
    
for i in range(b):
    print("|"*c,a,"|"*c,"\n", end='')


for i in range(c)[::-1]:
    print("|"*(i),"+","-"*(length+2*c-2*i),"+","|"*(i),sep='')
    
    


