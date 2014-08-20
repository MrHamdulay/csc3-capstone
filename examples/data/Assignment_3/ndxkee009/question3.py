#Keegan Naidoo
#NDXKEE009

m=input("Enter the message: \n")

r=int(input("Enter the message repeat count: \n"))

ft=int(input("Enter the frame thickness: \n"))

l=len(m)

es=""

for i in range(ft):
    
    y=es+"+"+"-"*(l+2*ft)+"+"+es
    print(y)
    es+="|"
    l+=-2
    
for j in range(r):
    
    z=es+" "+m+" "+es
    print(z)
    
a=es

b=len(es)-1

x=len(m)

#for i in range(ft):
    
  #  y=es+"+"+"-"*(l-2*ft)+"+"+es
   # print(y)
   # es+="|"
    #l+=2

for k in range(ft):
    
    #print(a[0:b])
    print(a[0:b]+"+"+"-"*(x+2)+"+"+a[0:b])
    
    #l+=2
    x+=2
    b+=-1
    