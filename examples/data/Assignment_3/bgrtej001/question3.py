#Question 3, Assignment 3
#Tejasvin Bagirathi

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
y = 0
x= len(message)+thick

for i in range(thick):
    print(y*"|", "+", (x+thick)*"-", "+", y*"|", sep="")
    y+=1
    x-=2
for j in range(repeat):
    print(thick*"|", message, thick*"|", sep = " ")
y=thick-1
x=len(message)+2
for k in range(thick):
    print(y*"|", "+", (x)*"-", "+", y*"|", sep="")
    y-=1
    x+=2    
    