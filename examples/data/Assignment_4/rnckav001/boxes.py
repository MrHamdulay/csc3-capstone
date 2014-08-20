#boxes
#Kavir Ranchod   -   RNCKAV001
#31/03/2014

def print_square ():
    """print rectangle of dimensions 5x5"""
    print("*****\n*   *\n*   *\n*   *\n*****")
    
def print_rectangle (w,h):
    """print rectangle of given dimensions"""
    print("*"*w)
    for i in range(h-2):
        print("*"+" "*(w-2)+"*")
    print("*"*w)
    
def get_rectangle (w,h):
    """return rectangle of given dimensions"""
        
    R=("*"*w+"\n"+("*"+" "*(w-2)+"*"+"\n")*(h-2)+"*"*w)
    return R
