def triangle():
    height = eval(input("Enter the height of the triangle:\n"))
    #gap = (height-height//2+(height//2-1))
    gap = height-1
    for i in range(0,height):
        
        print(gap*" ","*"*(2*i+1),sep="")
        gap-=1
        
if __name__=='__main__':
    triangle()
