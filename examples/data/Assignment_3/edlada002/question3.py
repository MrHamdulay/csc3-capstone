message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

width = len(message)+thickness*2+2


for i in range(thickness):
    print("|"*i, end="")
    print("+",(width-2-2*i)*"-","+", sep="",end="")
    print("|"*i)

for i in range (repeat):
     print("|"*thickness, end="")
     print(" "+message+" ",end="")
     print("|"*thickness)
    


for i in range(thickness-1,-1,-1):
    print("|"*i, end="")
    print("+",(width-2-2*i)*"-","+", sep="",end="")
    print("|"*i)

