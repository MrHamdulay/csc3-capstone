# box module
# badugela mulisa
# 1 April 2014


def print_square():
    print(5*'*')
    for i in range(5-2):
        print('*'+' '*(5-2)+'*')
    print(5*'*')

   

def print_rectangle(width,height):
    print(width*'*')
    for i in range(height-2):
        print('*'+' '*(width-2)+'*')
    print(width*'*')
    
def get_rectangle(width,height):  
    figure=(width*'*')+"\n"
    for i in range(height-2):
        figure+='*'+' '*(width-2)+'*'+"\n"
    figure+=(width*'*')+"\n"
        
    return figure
        
        

    

    
   
    


    
    