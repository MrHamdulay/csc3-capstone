""" defining box funictions
Bella Gorham
31 MARCH 2014"""

def print_square():
    print("*"*5)
    for i in range(3):
        print("*","*", sep="   ")
    print("*"*5)
    
    
def print_rectangle(w,h):
    print("*"*w)
    i=1
    while i<=h-2:
        print("*"+(w-2)*" " + "*")
        i+=1
    print("*"*w)
        
def get_rectangle(w,h):
    inner=""
    for i in range(h-2):
        line= "\n*" + (w-2)*" " + "*"
        inner+=line
    rect= "*"*w + inner + "\n*"+"*"*(w-1)
    return rect



    

if '___name___' == '___main___':

    print_square()
    print_rectangle(10,8)
    get_rectangle(8,8)
    





        