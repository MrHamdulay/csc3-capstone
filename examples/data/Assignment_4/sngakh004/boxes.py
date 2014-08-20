def get_rectangle(width,height): 
    t=width*"*"+"\n"
    f=""
    for i in range(height-2):
        f+="*"+(width-2)*" "+"*"+"\n"
    q=width*"*"
    return(t+f+q)

    
def print_rectangle(width,height):
    print(width*"*")
    for i in range(height-2):
        print("*","*",sep=(width-2)*" ")
    print(width*"*")
 
def print_square():
    print(5*'*')
    for i in range(3):
        print('*','*',sep=3*" ")
    print(5*'*')   
    

    
        