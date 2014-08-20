m = input("Enter the message:\n")
r = eval(input("Enter the message repeat count:\n"))
ft = eval(input("Enter the frame thickness:\n"))
cnt = 2*ft
for j in range(ft):    
    print("|"*j, "+", (len(m) + cnt)*"-", "+", "|"*j, sep="")
    cnt-=2
    
for i in range(r):
    print("|"*ft, " ",m," ","|"*ft, sep="")

cnt = 0    
for j in range(ft,0,-1):
    print("|"*(j-1), "+", (len(m)+ 2 + cnt)*"-", "+", "|"*(j-1), sep="")
    cnt+=2
            
    
