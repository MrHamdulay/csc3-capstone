def main():
    
    height= eval(input("Enter the height of the triangle:\n"))
    
    i=0
    x='*'

    gap= (height-1)
    
    for i in range(height):
        print(gap*" ", end="")
        gap=gap-1
        print(x)
        x=x+2*'*'
        i=i+1
        
main()
        
