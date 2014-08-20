#Question 1

def print_square():
    print("*"*5)
    i= 0
    while i < 3:
        mid= "*"+ "   "+"*"
        print(mid)
        i+=1
    print("*"*5) 
    
#===========part 2==========
def print_rectangle(width,height):
    print("*"*width)
    i=0
    while i <(height-2):
        mid= "*"+ " "*(width-2)+"*"
        print(mid)
        i+=1
    print("*"*width)  
    
#print_rectangle(5,7)       
        
        
#==========part 3===========
def get_rectangle(width,height):
    angle= "*"*width +"\n"
    i= 0
    while i < height-2:
        angle+= ("*" + " "*(width-2) + "*\n")
        i+=1
    angle+= ("*"*width)
    return angle
    
        
       
