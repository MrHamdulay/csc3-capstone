def print_square():
    print("*****")
    for i in range(3):
        print("*   *")
    print("*****")
    
def print_rectangle(width, height):
    print(width*'*')
    for i in range(height-2):
        print('*'+' '*(width-2)+'*')
    print(width*'*')
    
def get_rectangle(width,height):
    string = (width*'*')+'\n'
    for i in range(height-2):
        string += ('*'+' '*(width-2)+'*')+'\n'
    string += ('*'*width)+'\n'
    return string
