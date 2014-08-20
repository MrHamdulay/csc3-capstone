# Assignment 3
#program to draw a frame (made of the characters +-|) around a message 
# by TSHKAR003 (Karidas)

x=input("Enter the message: \n")
y=eval(input("Enter the message repeat count: \n"))
b=eval(input("Enter the frame thickness: \n"))

d=len(x)+2+2*b

for i in range(b):
    print("|"*i,"+",(d-(2*i)-2)*"-","+", "|"*i,sep="")
    
   
for i in range(y):
    print("|"*b,x,"|"*b)
    
for i in range(b)[::-1]:
    print("|"*i,"+",(d-(2*i)-2)*"-","+", "|"*i,sep="")    
       
    