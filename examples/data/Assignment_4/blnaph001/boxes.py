
def print_square():
    print("*****")
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')

def print_rectangle(x,height):
    print('*'*x)
    gaps=x-2
    for i in range(height-2):
        print('*'+' '*gaps+'*')
    print('*'*x)

def get_rectangle(x,height):
    box_string='*'*x+'\n'
    for i in range(height-2):
        box_string+='*'
        for i in range(x-2):
            box_string+=' '
        box_string+='*\n'
    box_string+='*'*x

    return box_string


