def print_square():
    for i in range (5):
        if(i==0) or (i==4):
            print(5*"*")
        else:
            print("*   *")

def print_rectangle(width,height):
    for i in range(height):
        if(i==0) or (i==(height-1)):
            print(width*"*")
        else:
            print("*"+(width-2)*" "+"*")

def get_rectangle(width,height):
    rec=""
    for i in range(height):
            if(i==0) or (i==(height-1)):
                rec= rec+ (width*"*")
             
            else:
                rec= rec+("*"+(width-2)*" "+"*")   
                
            rec= rec+ "\n"
    return rec