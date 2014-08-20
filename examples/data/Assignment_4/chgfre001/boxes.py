#program to print shapes of given height and width
#by chigwaza frederick
#03 april 2014

def print_square():
    #h=eval(input('Enter the height of the square:\n'))
    #w=eval(input('Enter the width of the square:\n'))
    
    for i in range(0,1):
        print('*'*5)
    for i in range(1,4):
        print('*'+' '*3+'*')
    for i in range(4,5):
        print('*'*5)
        
if __name__=="__main__":        
    print_square()

def print_rectangle(width,height):
    #w=eval(input('Enter the width of the rectangle:\n'))
    #h=eval(input('Enter the height of the rectangle:\n'))
    
    print('*'*width)
    
    for i in range(height-2):
        print('*'+' '*(width-2)+'*')
        
    print('*'*width)    

if __name__=="__main__":        
    print_rectangle(width,height)

def get_rectangle(width,height):
    #w=eval(input('Enter the width of the rectangle:\n'))
    #h=eval(input('Enter the height of the rectangle:\n'))
    
    x=('*'*width+'\n')
    
    for i in range(height-2):
        x=x+('*'+(' '*(width-2))+'*'+'\n')
        
    x=x+('*'*width)
    
    return (x)

if __name__=="__main__":
    get_rectangle(width,height)
    
    
    
    
    
    
    
        

    
    
    
        
        
       
        

    

        
    

    

    
        
       
