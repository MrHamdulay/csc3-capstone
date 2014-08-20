#2014-04-01
#Nkuna peter: NKNPET001
#module for boxes

def print_square():
    print("*"*5)
    for i in range(3):
        print("*"+" "*3+"*")
    print("*"*5)
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"+" "*(width-2)+"*")
    print("*"*width)

def get_rectangle(width,height):
    x="*"*width+"\n"
    t=height-2    
    y="*"+" "*(width-2)+"*"+"\n"
    y=y*t
    return x+y+x