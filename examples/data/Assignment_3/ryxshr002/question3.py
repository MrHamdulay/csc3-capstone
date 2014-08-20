def main():
    x=input("Enter the message: \n")
    y=eval(input("Enter the message repeat count: \n"))
    z=eval(input("Enter the frame thickness: \n"))
    a="+"
    n=(z*2)+ len(x)
    b=("-")

 
    for i in range (z):
        print("|"*i, end="")
        print(a, end='')
        print(b*n, end='')
        print(a,end="")
        print("|"*i)
        n=n-2
        
        
    for i in range(y):
        gap=1
        print(gap*"|"*z,x, gap*"|"*z)
    
    for i in range (z,0,-1):
        print("|"*(i-1), end="")
        print(a, end='')
        print(b*(n+2), end='')
        print(a,end="")
        print("|"*(i-1))
        n=n+2
        
        
    
    
    
    
main()