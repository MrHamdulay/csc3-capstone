def print_square():
    print("*"*5)
    print("*","*",sep="   ")
    print("*","*",sep="   ")
    print("*","*",sep="   ")
    print("*"*5)


def print_rectangle(w,h):
    #w=eval(width)
    #h=eval(height)
    print("*"*w)
    while h>2:
        print("*","*",sep=" "*(w-2))
        h-=1
    print("*"*w)
    
def rectangle(w,h):
    #w=eval(width)
    #h=eval(height)
    w1=("*"*w)
    while h>2:
        a='"*","*",sep=" "*(w-2)'
        p=a
        h-=1
        

def get_rectangle(w,h):
    num1="*"*w
    num2="*"*w
    while h>2:
        a="*"
        b="\n"
        d=" "
        c=w-2
        bx=a*w+b+(a+c*d+a+b)*(h-2)+a*w
        h-=1
        return(bx)
    
        
    #return("*"*w)
    
#print(get_rectangle(4,5))
