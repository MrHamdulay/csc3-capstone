#Kate Bell
#BLLKAT005
# 2 April 2014

def print_square():
    print("*"*5)
    for i in range (0,3):
        print("*","   ","*",sep="")
    print("*"*5) 
        
        
def print_rectangle (width, height):
    for i in range (0,height):
            if i==0 or i==height-1:
                print("*"*width)
            else:
                print("*"," "*(width-2),"*",sep="")
        
def get_rectangle (width, height):
    strBox=""
    for i in range (0,height):
                if i==0:
                    strBox=strBox+"*"*width+"\n"
                elif i<height-1 and i>0:
                    strBox=strBox+"*"+" "*(width-2)+"*"+"\n"
                elif i==height-1:
                    strBox=strBox+"*"*width
    return strBox

       
