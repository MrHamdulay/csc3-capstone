a=eval(input("Enter the cost (in cents):\n"))
while a<0:
    a=eval(input("Enter the cost (in cents):\n"))
    
if a==0:
   a=eval(input("Enter the cost (in cents):\n")) 


b=eval(input("Deposit a coin or note (in cents):\n"))
b=b
while b<a:
    
    l=eval(input("Deposit a coin or note (in cents):\n")) 
    b=b+l 

j=b-a      
m=b-a
if m>0:
    j=b-a
    print("Your change is:")
if b>=0 :
    k=j//100

    if k>=1:
        
        print(k,"x $1")

    d=j-k*100
    if d>=25:
        h=d//25
        print(h,"x 25c")
    
    f=d%25
    if f>=10:
        z=f//10
        print(z,"x 10c")
    
    u=d%25
    if 5<=u<10:
        print("1 x 5c")
    
    n=u%5
    if 1<=n<5:
        print(n,"x 1c")
    
