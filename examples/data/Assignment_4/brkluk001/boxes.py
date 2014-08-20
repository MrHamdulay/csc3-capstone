def print_square():
    print('*' * 5)
    for j in range(3):
        print('*' , " "*3 , '*' , sep="")
    print('*' * 5)  
    
    
    
    
def print_rectangle(width, height):
    print('*' * width)
    gap = " "
    for i in range(height -2):
        print('*' , gap * (width-2) , '*', sep="")
    print('*' * width)
    
def get_rectangle (width, height): 
    new='\n'
    star='*'
    figure=""
    firstline = (star*width) + new
    lastline = (star*width)
    gap=" "
    
    middle=""
    
    for i in range(height-2):
        line=star+(gap*(width-2))+star+new
        middle+=line
        
    figure = firstline + middle + lastline
    
    return figure
        
    
    
    
    
        
    
    
    




        
        
    
        
        

        
        
        
        
         
        
        
        
    
    
    
    
