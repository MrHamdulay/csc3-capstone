#Raeesa Behardien
#BHRRAE003
#Assignment 3 - 28 March 2014

#Question 3
#Programe to draw a frame around a message

msg=input("Enter the message:" '\n')
y=eval(input("Enter the message repeat count:" '\n')) 
x=eval(input("Enter the frame thickness:" '\n'))
a=1
b=0
c=0
d=x
for i in range(x):
    print("|"*(x-d),"+","-"*(len(msg)+(x*2)+c),"+","|"*(x-d),sep="") 
    d-=1
    c-=2
for i in range(y):
    print("|"*x,msg,"|"*x)
for i in range(x):
    print("|"*(x-a),"+","-"*(len(msg)+(b+2)),"+","|"*(x-a),sep="")
    a+=1
    b+=2
    


