def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width,height):
    print(width * "*")
    for i in range(height-2):
        print("*"+(width-2)*" "+"*")
    print(width * "*")
    
def get_rectangle(width,height):
    x = (width * "*")+"\n"
    y = (width * "*")
    for i in range(height-2):
        x+="*"+(width-2)*" "+"*"+"\n"
    return x+y
        


    
    
    