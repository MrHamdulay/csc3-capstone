def print_square():
    
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width,height):
    t="*"
    print(t*width)
    for i in range(height):
        print(t+(" "*(width-2))+t)
    print(t*width)

def get_rectangle(width,height):
    t = "*"
    rectangle = t*width + "\n" + height*(t+(" "*(width-2))+t+ "\n")  + t*width
    return rectangle
    


          