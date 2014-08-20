#boxes:
def print_square():
    box="{0}{0}{0}{0}{0}\n{0}{1}{1}{1}{0}\n{0}{1}{1}{1}{0}\n{0}{1}{1}{1}{0}\n{0}{0}{0}{0}{0}"
    print(box.format("*"," "))
    return
#print_square()

#rectangle
def print_rectangle (width, height):
    print("*"*width)
    for i in range((height-2)):
        print("*"," "*(width-2),"*", sep="")
    print("*"*width)
    return
#width=eval(input("width: "))
#height=eval(input("height: ")) 
#print_rectangle(3,5)

def get_rectangle (width, height):
    a="*"*width + "\n"
    b =''
    for i in range((height-2)):
        b= b +"*"+" "*(width-2)+"*"+"\n"
    c="*"*width
    box = a+b+c
    return box

#width=eval(input("widtht: "))
#height=eval(input("height: "))    
get_rectangle(3,4)
    
    