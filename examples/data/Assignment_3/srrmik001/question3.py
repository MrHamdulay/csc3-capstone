
x = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))


for depth in range(z):
    print("|"*depth+"+"+"-"*(len(x)+2*(z-depth-1)+2)+"+"+"|"*depth)
for repeat in range(y):
    print("|"*z+" "+x+" "+"|"*z)
for depth in reversed (range(z)):
    print("|"*depth+"+"+"-"*(len(x)+2*(z-depth-1)+2)+"+"+"|"*depth)