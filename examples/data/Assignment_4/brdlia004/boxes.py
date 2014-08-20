def print_square():
    print(5*"*")
    for i in range(5-2):
        print("*"+" "*(5-2)+"*")
    print(5*"*")

def print_rectangle(width, height):
    print(width*"*")
    for i in range(height-2):
        print("*"+" "*(width-2)+"*")
    print(width*"*")

def get_rectangle (width, height):
    if height != 2:
        box = width*"*"
        box += "\n*"+" "*(width-2)+"*\n"
        for i in range(height-3):
            box += "*"+" "*(width-2)+"*\n"        
        box += width*"*"
        return(str(box))
    else:
        box = ""
        for i in range(height):
            box += "*"+" "*(width-2)+"*\n"
        return(str(box))        
        
  
