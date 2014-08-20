def print_square():
    print("*"*5)
    for i in range(3):
        print("*", " "*3, "*", sep="")
    print("*"*5)
        
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2), "*", sep="")
    print("*"*width)
    

def get_rectangle(width, height):
    string1="*"*width+"\n"
   # for i in range(height-2):
    string2=("*"+" "*(width-2)+"*"+"\n")*(height-2)
    string3="*"*width+"\n"
    return string1 + string2 + string3