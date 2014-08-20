def print_square ():
    gap=(" ")
    print("*"*5)
    print("*",gap,"*")
    print("*",gap,"*")
    print("*",gap,"*")
    #print("*",gap,"*")
    print("*"*5)
    
def print_rectangle(width,height):
    x=(width)
    y=(height)
    gap=(x-2)
    i=(0)
    print("*"*x)
    for i in range(y-2):
        print("*"," "*gap,"*",sep="")
        i+=1
    print("*"*x)

def get_rectangle(width,height):
    
    x=(width)
    y=(height)
    gap=(x-2)
    a="*"*x+"\n"
    #print (a)
    b=("*"+" "*gap+"*"+"\n")
    
    return a+b*(y-2)+a

#get_rectangle(5,6)