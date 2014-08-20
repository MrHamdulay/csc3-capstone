# question1.py
# author: bxtnaa002

def print_square():
    for i in range(1,6):
        if i == 1 or i == 5:
            print("*"*5)
        else:
            print("*"," "*3,"*", sep="")
            
        
def print_rectangle(width, height):
    for j in range(1,height+1):
        if j == 1 or j == height:
            print("*"*width)
        else:
            print("*", " "*(width-2), "*", sep="")
            

def get_rectangle(width, height):
    y= ("*"*width + "\n")
    x=0
    while x<height-2:
        y+= ("*"+(" "*(width-2)+"*")+"\n")
        x+=1
           
    y+= ("*"*width)
    return (y)    
            
            
