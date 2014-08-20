def print_square():
    print(5*("*"))
    for i in range(3):
        print("*"+"   "+"*")
    print (5*("*"))      


def print_rectangle(width, height):
    if height==1:
        print((width)*("*")) 
    elif height==2:
        print((width)*("*"))
        print((width)*("*"))
    elif height>2:
        print(width*("*"))
        for i in range(height-2): 
            if width==1:
                print("*") 
            elif width==2:
                print("**")
            elif width>2:
                print(("*")+(width-2)*(" ")+("*"))
        print(width*("*")) 
        
        
def get_rectangle(width,height): 
    if height==1:
        string =((width)*("*")) 
    elif height==2:
        string =((width)*("*")+"\n")
        string =((width)*("*")+"\n")+((width)*("*")+"\n")
    elif height>2:
        string1 =(width*("*")+"\n")
        string3 =""
        for i in range(height-2): 
            if width==1:
                string2 =("*")+"\n" 
            elif width==2:
                string2 =("**")+"\n"
            elif width>2:
                string2 =(("*")+(width-2)*(" ")+("*"))+"\n"
                string3 = string3+string2
        string4 =(width*("*"))
        string = string1+string3+string4
    return string 
    
    
    