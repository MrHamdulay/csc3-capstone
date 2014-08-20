x=input("Enter the message:\n")

repeat=eval(input("Enter the message repeat count:\n"))

thick=eval(input("Enter the frame thickness:\n"))

y=len(x)+2*thick
z=len(x)+2
gap=0
for i in range(y, z-2, -2):
        print("|"*gap, "+", "-"*i, "+", "|"*gap, sep="")
        gap+=1
for j in range(repeat):
        print("|"* thick, x.center(y-2*thick), "|"*thick)
gap=thick-1
for i in range(z, y+1, 2):
        print("|"*gap, "+", "-"*i, "+", "|"*gap, sep="")
        gap-=1