def print_square ():
    print('*'*5)
    for i in range (3):
        print('*   *')
    print('*'*5)
    
                
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
    

def get_rectangle(width,height):
    width=int(width)
    box=('*'*width)
    box2=""
    for i in range(height-2):
        box2+=("*"+" "*(width-2)+"*"+'\n')
    final_box=box +'\n' + box2 + box
    return final_box

#Sbonelo Mntungwa
#MNTSBO001
#Program to create boxes
#4 April 2014

    
    
    
    
    
