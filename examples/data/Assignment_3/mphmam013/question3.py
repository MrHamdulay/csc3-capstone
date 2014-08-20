def main():
    n=input("Enter the message: \n")
    m=eval(input("Enter the message repeat count:\n"))
    x=eval(input("Enter the frame thickness: \n"))
    
    for i in range(x):
        print("|"*i,'+',"-"*len(n),"-"*2*(x-i),'+',"|"*i,sep='')
    for i in range(m):
        print("|"*x,n,"|"*x)
    for i in range(x-1,-1,-1):
        print("|"*i,'+',"-"*len(n),"-"*2*(x-i),'+',"|"*i,sep='')    
    
main() 
        