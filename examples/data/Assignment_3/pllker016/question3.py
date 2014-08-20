m=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
k=0
p=t
for i in range(t, 0, -1):
    print("|"*k,"+", "-"*(len(m)+(i*2)), "+", "|"*k, sep = "")
    k+=1

for i in range(r):
    print("|"*t + " " + m + " " + "|"*t, sep = "")
    
for i in range(0, t):
    print("|"*(p-1),"+", "-"*(len(m)+((i)*2)+2), "+", "|"*(p-1), sep = "")
    p-=1