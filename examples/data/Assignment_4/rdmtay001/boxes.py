def print_square():
    print("*"*5)
    for x in range(3):
        print("*"," "*3,"*",sep="")
    print("*"*5)


if __name__=="__print_square__":
    print_square()


def print_rectangle(width,height):
    
    
    
    if height>0:
        print('*'*width)
    for x in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    if height>0:
        print("*"*width)
if __name__=="__print_rectangle__":
    print_rectangle
    
def get_rectangle(width,height):
    if height>0:
        first_and_last_line="*"*width+"\n"
        spaces=" "*(width-2)
        secondLine="*"+spaces+"*"+"\n"
        middleLines=secondLine*(height-2)
        BOX=first_and_last_line+middleLines+first_and_last_line
        return BOX
        
        
        