def print_square():
    gap=5-2
    print("*"*5)
    for i in range(5-2):
        print("*", " "*gap, "*", sep="")
    print("*"*5)

def print_rectangle(width, height):

    gap=width-2
    print("*"*width)
    for i in range(height-2):
        print("*", " "*gap, "*", sep="")
    print("*"*width)
    
def get_rectangle(width, height):
    gap=width-2
    box=""
    box+="*"*width+"\n"
    for i in range(height-2):
        box+="*"+" "*gap+"*"+"\n"
    box+="*"*width
    return box