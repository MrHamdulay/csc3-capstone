def main():
    m= input("Enter the message:\n")
    times= eval(input("Enter the message repeat count:\n"))
    thick= eval(input("Enter the frame thickness:\n"))
    y= len(m) + thick*2
    for i in range(0,thick):
        print("|"*i+"+"+"-"*y+"+"+"|"*i)
        y-=2
    for i in range(0,times):
        print(("|"*thick+" "+m+" "+("|"*thick)))
    mber= thick-1    
    mberi=len(m)+2
    for i in range(thick,0,-1):
        print("|"*mber+"+"+"-"*mberi+"+"+"|"*mber)
        mber-=1
        mberi+=2
        
main()        