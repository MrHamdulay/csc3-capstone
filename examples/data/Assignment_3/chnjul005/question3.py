m = input("Enter the message:\n")
mr = eval(input("Enter the message repeat count:\n"))
ft = eval(input("Enter the frame thickness:\n"))
linet = 0
dashn = len(m) +(ft*2) 
for i in range(ft):
    print("|"*linet,"+","-"*dashn,"+","|"*linet,sep="")
    linet+=1
    dashn-=2
    
for i in range(mr):
    print("|"*ft,m,"|"*ft)
linet-=1
dashn+=2
for i in range(ft):
    print("|"*linet,"+","-"*dashn,"+","|"*linet,sep="")
    linet-=1
    dashn+=2
    