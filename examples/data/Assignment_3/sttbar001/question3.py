name = input("Enter the message: \n")
r = eval(input("Enter the message repeat count: \n"))
t =eval(input("Enter the frame thickness: \n"))
l = len(name)
f =r+(2*t)
for i in range(f):
    if i<(t):
        print("|"*(i)+"+"+("-"*(l)+"-"*(((t)*2)-(i*2)))+"+"+"|"*(i))
        g=i
    elif i>=t and i<(t+r):
        print(("|"*(g+1))+" "+name+" "+("|"*(g+1)))
    elif i>=(t+r) :
        print("|"*g+"+"+("-"*(l)+"-"*(((t)*2)-(g*2)))+"+"+"|"*g)
        g=g-1