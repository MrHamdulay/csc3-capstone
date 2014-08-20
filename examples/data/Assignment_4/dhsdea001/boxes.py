#Question 1
#By: Dean de Haast

def print_square():
    print("*"*5)
    print("*"," "*3,"*",sep="")
    print("*"," "*3,"*",sep="")
    print("*"," "*3,"*",sep="")
    print("*"*5)
    
def print_rectangle(width,height):
    print(width*"*")
    for x in range(1,(height-1)):
        print("*"," "*(width-2),"*",sep="")
    print(width*"*")
    
def get_rectangle (width, height):
    figure= width*"*"+"\n"
   
    for x in range(1,(height-1)):
        figure=figure+ "*"+(" "*(width-2))+"*"+"\n"
    figure=figure+(width*"*")+"\n"    
    
    return(figure)
  