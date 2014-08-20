def print_square():
    for i in range (5):
        if i == 0 or i ==4:
            print("*****")
        else:
            print("*   *")


def print_rectangle(width,height):
    for i in range (height):
        if i == 0 or i == height-1:
            print("*"*width)
        else:
            print("*"," "*(width-2),"*", sep="")

def get_rectangle(width,height):
    i = 2
    box = "*"*width
    while i < height:
        box = box + "\n" + "*" + (" "*(width-2)) + "*"
        i = i+1
    box = box + "\n" + "*"*width
    return box 
   
        

        
