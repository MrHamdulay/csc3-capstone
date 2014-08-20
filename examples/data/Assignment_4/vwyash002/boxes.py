def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
    
def print_rectangle (width, height):
        
        print("*"* width)
        
        gaps = width-2
        i=0
        for i in range(height):
                print("*"+ gaps*" " +"*")
                i+=1
            
        print("*"* width)
        
        
def get_rectangle(width, height):
    for i in range(1,height+1):
            if i == 1: output = ("*"*width)+"\n"
            elif i == height: output+=("*"*width)+"\n"
            else: output+=("*"+" "*(width-2)+"*")+"\n"
    return output
