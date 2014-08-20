def print_square():
    print(5*"*",sep="")
    print("*"," ","*")
    print("*"," ","*")    
    print("*"," ","*")    
    print(5*"*",sep="")
    
def print_rectangle(w,h):
    print(w*"*",sep="")
    for i in range(1,h-1):
        print("*",(w-2)*" ","*",sep="")
    print(w*"*",sep="")
    
def get_rectangle(w,h):
    recta=w*"*"
    rectc=w*"*"
    if h>1:
        out2="{0}\n{1}\n{2}"    
        out1="{0}\n{1}"
        if h>2:
            rectb="*"+(w-2)*" "+"*"
            for i in range(h-3):
                rectb=out1.format(rectb,"*"+(w-2)*" "+"*")
                
            rect=out2.format(recta,rectb,rectc)
            return(rect)
        else:
            rect=out1.format(recta,rectc)
            return(rect)
    else:
        return(recta)
    

