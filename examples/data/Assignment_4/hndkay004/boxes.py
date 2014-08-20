def print_square():
    print('*'*5)
    for i in range(3):
        print('*',' '*3,'*',sep='')
    print('*'*5)

def print_rectangle(width,height):
    print('*'*width)
    for i in range(height-2):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)

def get_rectangle (width,height):
    x=''
    a=('*'*width)+'\n'
    b=''
    for i in range(height-2):
        stars='*'+' '*(width-2)+'*'+'\n'
        b=b+stars
    c='*'*width
    x= a+b+c
    return x
        
   
   



    
    

    
    
    
