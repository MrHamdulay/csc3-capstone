def print_square ():
        print('*'*5)
        for y in range(3):
                print('*',' '*3,'*',sep='')
        print('*'*5)        
       
def print_rectangle (width,height):
        print('*'*width)
        for y in range(height-2):
                print('*',' '*(width-2),'*',sep='')
        print('*'*width)
              
def get_rectangle (width,height):
        x=''
        x=x+(('*'*width)+'\n')
        for y in range(height-2):
                x=x+('*'+' '*(width-2)+'*'+'\n')
        x=x+('*'*width+'\n')
        return x     
