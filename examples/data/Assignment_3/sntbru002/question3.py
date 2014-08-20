def main():
    a = input("Enter the message:\n")
    b = eval(input("Enter the message repeat count:\n"))
    c = eval(input("Enter the frame thickness:\n"))
    d = '+'
    e = '-' 
    for i in range(0,c):
        w = len(a)+2+(2*c)
        print(('|'*i)+d+(e*(w-(2*(i+1))))+d+('|'*i))
    for i in range(b):
        print(('|'*c ),a,('|'*c))
    for i in range(c-1,-1,-1):
        print(('|'*i)+d+(e*(w-(2*(i+1))))+d+('|'*i))
        
main()        
                  
       
        