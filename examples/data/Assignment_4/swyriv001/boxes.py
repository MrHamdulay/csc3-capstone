def print_square ():
    y=1
    x=5
    j=3
    
    print("*"*x)
    print(end="")
    for i in range(1,4):
        print("*"*y,end="")
        print(" "*j,end="")
        print("*"*y)
    print(end="")
    print("*"*x)
    
    
def print_rectangle (width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"*1,end="")
        print(" "*(width-2),end="")
        print("*"*1)
    print("*"*width)
    
    
def get_rectangle (width, height):
    x=""
    x+="*"*width+"\n"
    for i in range(height-2):
        x+="*"+" "*(width-2)+"*"+"\n" 
    x+="*"*width
   
    return  x
#print(get_rectangle (4,5))
  