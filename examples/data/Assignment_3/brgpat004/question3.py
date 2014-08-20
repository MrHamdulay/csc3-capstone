message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
tempthick=thickness
count=0
for i in range(thickness):
        print("|"*count,"+","-"*(len(message)+2*tempthick),"+","|"*count,end="",sep="")
        tempthick-=1
        count+=1
        print()
    
for i in range(repeat):
        print("|"*thickness,message,"|"*thickness)
count-=1
tempthick+=1
for i in range(thickness):
        print("|"*count,"+","-"*(len(message)+2*tempthick),"+","|"*count,end="",sep="")
        tempthick+=1
        count-=1
        print()   