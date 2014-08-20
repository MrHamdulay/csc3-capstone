#File name: boxes.py
def print_square():
        print("*"*5)
        print("*" + " "*3 +"*")
        print("*" + " "*3 +"*")
        print("*" + " "*3 +"*")
        print("*"*5)



def print_rectangle (width,height):
        for i in range (0,1):
            print("*" * width)
        for i in range (0,(height-2)):
            print("*" + ' ' * (width-2) + "*" )
        for i in range (0,1):
            print("*" * width)    
        
def get_rectangle (width,height):
        new = []
        a = new.append(str("*"*width))
        for n in range(1,height-1):
                a= new.append(str("*"+" "*(width-2)+"*"))
        a = new.append(str("*"*width))
        b = '\n'.join(new)
        return(b)


