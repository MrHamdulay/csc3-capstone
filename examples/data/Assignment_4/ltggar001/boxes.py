def print_square():
    q="*   *\n"
    print("*"*5,"\n",q*3,"*"*5,sep="")
def print_rectangle(width,height):
    print("*"*width)
    w=width-2
    e=height-2
    r=0
    while r<e:
        print("*"," "*w,"*",sep="")
        r+=1
    print("*"*width)
def get_rectangle(width,height):
    top="*"*width+"\n"
    middle="*"+" "*(width-2)+"*"+"\n"
    bottom="*"*width
    return top + middle*(height-2) + bottom