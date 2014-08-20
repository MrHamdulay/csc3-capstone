x = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))

top  = 0
length = len(x)+z*2


for a in range(z):
    print(top*("|"),"+",length*("-"),"+",top*("|"),sep="")
    length -=2
    top+=1
    
for b in range(y):
    print(("|")*z,x,("|")*z)
    
lennew = len(x)+2
vert = z-1
for c in range(z):
    print(vert*("|"),"+",lennew*("-"),"+",vert*("|"),sep="")
    lennew +=2
    vert -=1