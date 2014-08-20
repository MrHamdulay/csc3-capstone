x = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))
for top in range(z):
    print("|"*top+"+"+"-"*(len(x)+2+(z-1)*2-top*2)+"+"+"|"*top)
for repeat in range(y):
    print("|"*z+" "+x+" "+"|"*z)
for top in reversed(range(z)):
    print("|"*top+"+"+"-"*(len(x)+2+(z-1)*2-top*2)+"+"+"|"*top)

