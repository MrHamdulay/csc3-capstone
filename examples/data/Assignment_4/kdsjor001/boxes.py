def print_square():
        print ('*****')
        for i in range(3):
                print('*   *')
        print('*****')
def print_rectangle(x,y):
        print('*'*x)
        for i in range (y-2):
                print('*'+' '*(x-2)+'*')
        print('*'*x)
def get_rectangle(x,y):
        outside='*'*x+'\n'
        inside=('*'+' '*(x-2)+'*'+'\n')*(y-2)
        box_c=outside+inside+outside
        return (box_c)