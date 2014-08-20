def main():
    a=input("Enter the message:\n")
    b=eval(input("Enter the message repeat count:\n"))
    c=eval(input("Enter the frame thickness:\n"))
    d=0
    min=(len(a)+2)
    for i in range(1,c,1):
        min+=2
    for i in range(c):
        print(d*"|","+","-"*min,"+","|"*d,sep="")
        min-=2
        d+=1
    for i in range(b):
        print("|"*c,a,"|"*c)
    
    for i in range(c):
        d-=1 
        min+=2
        print(d*"|","+","-"*min,"+","|"*d,sep="")
        
       
main()
        
    
    
    
    