# Shaaheen Sacoor
# 31 March 2014
def print_square():
    print("*"*5)
    print("*","   ","*",sep="")
    print("*","   ","*",sep="")
    print("*","   ","*",sep="")
    print("*"*5)

def print_rectangle(w,h):
    
    t=1
    sq = ("*"*w)
    square= (sq+"\n")
    if w == 1:
        while t<=(h-2):
                square += ("\n*")
                square+= (" "*(w-2))
                t+=1
    else:
        while t<=(h-2):
            square += ("*")
            square += (" "*(w-2))
            square += ("*\n")
            t+=1
    square +="*"*w
    print(square)

def get_rectangle(w,h):
    t=1
    sq = ("*"*w)
    square= (sq+"\n")
    if w == 1:
        while t<=(h-2):
                square += ("\n*")
                square+= (" "*(w-2))
                t+=1
    else:
        while t<=(h-2):
            square += ("*")
            square += (" "*(w-2))
            square += ("*\n")
            t+=1
    square +="*"*w
    return square
    
get_rectangle(4,3)
          

