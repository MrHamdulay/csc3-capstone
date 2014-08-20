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
    new_line='\n'
    star='*'
    figure=""
    top_line=(star*width)+new_line
    bottom_line=(star*width)
    gap=" "
    middle=""
    for i in range(height-2):
        line=star+(gap*(width-2))+star+new_line
        middle+=line
        
    figure=top_line + middle + bottom_line 
    return figure