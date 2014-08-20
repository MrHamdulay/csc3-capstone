# boxes.py
# Womgwa Giqwa
# 01 April 2014 boxes():
def print_square():
    print('*'*5)
    for i in range(3):
        print('*'+' '*3+'*')
    print('*'*5)
#print_square()


def print_rectangle(width, height):
        #width=eval(input())
        #height=eval(input())
    s=((width)-2)
        
    print('*'*width)
    for i in range(height-2):
        print('*'+' '*s+'*')
    print('*'*width)
#print_rectangle(10,10)
    
def get_rectangle(width, height):
    s=((width)-2)
    b=''
    b+='*'*width+'\n'
    for i in range(height-2):
        b+='*'+' '*(s)+'*'+'\n'
    b+='*'*width
    return b
   
                
#print(get_rectangle(6,7))
                
                
    


   
        
    
        
        
    
    