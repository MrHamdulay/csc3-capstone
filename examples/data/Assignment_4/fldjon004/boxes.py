def print_square():
    print('*' * 5)
    for i in range(3):
        print('*' , " "*3 , '*' , sep="")
    print('*' * 5)  
    
    
    
def print_rectangle(width, height):
    print('*' * width)
    gap = " "
    for i in range(height -2):
        print('*' , gap * (width-2) , '*', sep="")
    print('*' * width)
    
def get_rectangle (width, height): 
    newline='\n'
    star='*'
    figure=""
    first_line=(star*width)+newline
    last_line=(star*width)
    gap=" "
    
    middle=""
    
    for i in range(height-2):
        line=star+(gap*(width-2))+star+newline
        middle+=line
        
    figure=first_line + middle + last_line
    
    return figure