#2 April 2014
#Shaun Muzenda
#Creating different kinds of hollow boxes of stars

def print_square ():
    print('*'*5)
    for i in range (3):
        print('*', ' ', '*')
    print('*'*5)   
    

def print_rectangle (width, height):
    if height > width:
        print('*'*width)
        for i in range ((height-width)+1):
            print('*'+' '*(width-3),'*')
        print("*"*width)
            
    elif width > height:
        print('*'*width)
        for i in range ((height-2)):
            print('*'+' '*(width-3),'*')
        print("*"*width)  
        
    elif width == height:
        print('*'*width)
        for i in range ((height-2)):
            print('*'+' '*(width-3),'*')
        print("*"*width)         


def get_rectangle (width, height):
    figure = (width * "*"+"\n")   
    for x in range(1,(height-1)):
        figure = figure+("*")+(" " * (width-2))+("*")+("\n")
    figure = figure+(width * "*")       
    return(figure)
