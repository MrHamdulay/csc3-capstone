def print_square():
    print("*"*5)
    for i in range(1,4):
        print("*"," ","*")
    print("*"*5)
    return

#print_square()   

def print_rectangle(width,height):
    print("*"*width)
    height-=2
    for i  in range(height):
        n=width-2
        print("*"+" "*n+"*")
    print("*"*width)
    return
#print_rectangle(3,4)

def get_rectangle(width,height):
    first_line="*"*width+"\n"
    height-=2
    for i  in range(height):
        n=width-2
        middle="*"+" "*n+"*"+"\n"
    middles=middle*height
    last_line="*"*width+"\n" 
    rectangle=first_line+middles+last_line
    #print(rectangle)
    return rectangle
#get_rectangle(3,5)






        
