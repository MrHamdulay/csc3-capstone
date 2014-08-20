x=input("Enter the message:"'\n')
y=input("Enter the message repeat count:"'\n')
z=input("Enter the frame thickness:"'\n')
x = " %s "%x # Add the spaces
for depth in range(eval(z)):
    # depth will be 0 on the first iteration, then 1
    print("|"*depth+"+"+"-"*(len(x)+2*(eval(z)-depth-1))+"+"+"|"*depth)
for repeat in range(eval(y)):
    print("|"*eval(z)+x+"|"*eval(z))
for depth in reversed(range(eval(z))):
    # reverse the depth values to start from the inner frame
    print("|"*depth+"+"+"-"*(len(x)+2*(eval(z)-depth-1))+"+"+"|"*depth)




