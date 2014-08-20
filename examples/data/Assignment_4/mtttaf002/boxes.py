def print_square():
    for i in range(5):
        if i == 0 or i == 4:
            print("*"*5)
        else:
            print("*"+" "*3+"*")
    
def print_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height-1:
            print("*"* width)
        else:
            print("*"+" "*(width-2)+"*")
                
def get_rectangle(width, height):
    temp = ""
    for i in range(height):
        if i == height-1:
            temp += ("*"*width)
        elif i == 0:
            temp += ("*"* width+"\n")
        else: temp += ("*"+" "*(width-2)+"*" + "\n")
        
    return temp


         
        
        
            