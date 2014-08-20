#bishum



def print_square():                      
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*",sep="")
    print("*"*5)

def print_rectangle(width, height):             #to ask in cs lab after
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)    

def get_rectangle(width,height):          #page 46 pthon mru version
    string=""
    string+=string+("*"*width)+"\n"
    for i in range(height-2):
        string+="*"+(" "*(width-2))+"*\n"
    string+=("*"*width)+"\n"
    return string
