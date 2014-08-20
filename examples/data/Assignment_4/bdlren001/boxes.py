# Box
# BDLREN001
# Budeli Rendani
# 30 March 2014

def print_square(): #printing square
    print(5*'*')
    
    for j in range(5-2):
        
        print('*'+' '*(5-2)+'*')
    
    print(5*'*')

def print_rectangle(width,height): #printing rectangle
    
    print(width*'*')
    
    for j in range(height-2):
        
        print('*'+' '*(width-2)+'*')
    
    print(width*'*')
    
def get_rectangle(width,height):  
    
    figure=(width*'*')+"\n"
    
    for j in range(height-2):
        
        figure+='*'+' '*(width-2)+'*'+"\n"
    
    figure+=(width*'*')+"\n"
        
    return figure
        
        

    

    
   
    


    
    