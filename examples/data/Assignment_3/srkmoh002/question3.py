# question3.py

message=input("Enter the message:\n")                    
count=eval(input("Enter the message repeat count:\n"))   
thick=eval(input("Enter the frame thickness:\n"))              
    
# top part
b=thick
for i in range(thick):
    print((i*"|"),"+",(len(message)+b*2)*"-","+",(i*"|"),sep="")
    b=b-1

# middle part
for i in range(count):
    print(thick*"|",message,thick*"|")
    
# bottom part
b=1
for i in range(thick):
    print(((thick-(i+1))*"|"),"+",(len(message)+b*2)*"-","+",((thick-(i+1))*"|"),sep="")
    b=b+1
