def print_square():
        x = "*****"
        y = "*"
        print(x)
        for i in range(3,0,-1):
                print(y,"   ",y,sep="")
        print(x)
        
def print_rectangle(width,height):
        v = '*'
        print(v*width)
        for i in range(height-2,0,-1):
                print((v+(' '*(width-2))+v),sep='')
        print(v*width)
   
def get_rectangle(width,height):
        f = '*'
        print(f*width)
        for j in range(height-2,0,-1):
                print(f+(' '*(width-2))+f)
        print(f*width)            

        
     