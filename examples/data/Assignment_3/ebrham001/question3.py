x=input("Enter the message:\n")

msg=eval(input("Enter the message repeat count:\n"))

thick=eval(input("Enter the frame thickness:\n"))

a=len(x)+2*thick
z=len(x)+2
gap=0
for i in range(a,z-2,-2):
    print("|"*gap, "+", "-"*i, "+", "|"*gap, sep="")
    gap+=1
for j in range(msg):
    print("|"*thick, x.center(a-2*thick), "|"*thick)
    gap=thick-1
for i in range(z, a+1, 2):
    print("|"*gap, "+", "-"*i, "+", "|"*gap, sep="")
    gap-=1