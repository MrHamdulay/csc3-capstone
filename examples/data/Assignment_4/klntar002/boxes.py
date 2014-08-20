# box of 5 x 5
# tarisai kalinde
# klntar002

def print_square():
    print('*****')
    for i in range(3):
        print('*   *')
    print('*****')

if __name__=='__main__':
    print_square



def print_rectangle(width,height):
    height=height-2
    ww=width-2
    print('*'*width)
    for i in range(height):
        print('*',' '*ww,'*',sep='')
    print('*'*width)
    
if __name__=='__main__':
    print_rectangle(width,height)



def get_rectangle(width,height):
    height=height-2
    ww=width-2
    n=('*'*width+'\n')
    for i in range(height):
        n=n+('*'+(' '*ww)+'*'+'\n')
    n=n+('*'*width)
    return n
    
  
   
   
        
    

if __name__=='__main__':
    get_rectangle(width,height)
    
    