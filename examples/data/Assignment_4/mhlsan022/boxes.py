'''This program prints squares and rectangles
SANDILE CHRISTOPHER MAHLANGU
1 APRIL 2014'''

def print_square ():
    print("*****")
    print('*   *','*   *','*   *',sep='\n')
    print("*****")
def print_rectangle (width, height):
    print('*'*width)
    for i in range(height-2):
        print('*'+' '*(width-2)+"*")
    print('*'*width)
def get_rectangle (width, height):
    c='*'*width+'\n'

    for i in range(height-2):
        c+='*'+' '*(width-2)+"*"'\n'
    c+='*'*width
    return c