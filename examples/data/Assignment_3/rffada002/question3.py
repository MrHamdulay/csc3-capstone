message = input("Enter the message:\n")
repeat_count = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

x=thickness
y=thickness-1
z=2

for i in range(thickness):
    print("|"*i+"+"+"-"*(len(message)+x*2)+"+"+"|"*i)
    x=x-1
    
for i in range(repeat_count):
    print("|"*thickness+" "+message+" "+"|"*thickness)
    
for i in range(thickness):
    print("|"*y+"+"+"-"*(len(message)+z)+"+"+"|"*y)
    y=y-1
    z=z+2