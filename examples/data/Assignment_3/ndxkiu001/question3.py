#question3
s = input("Enter the message:\n")
sr = eval(input("Enter the message repeat count:\n"))
ft = eval(input("Enter the frame thickness:\n"))
sl = len(s)
w = 2*ft+sl
h = ft*2+sr


for x in range(ft):
    print("|"*x,"+","-"*w,"+","|"*x,sep ="")
    w = w-2

for x in range(sr):
    print("|"*ft,s,"|"*ft)

w = w+2
for x in range(ft,0,-1):
    print("|"*(x-1),"+","-"*w,"+","|"*(x-1),sep ="")
    w = w+2
    

