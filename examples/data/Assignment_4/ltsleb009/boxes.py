

def print_square():
    print('*****\n','*   *\n','*   *\n','*   *\n','*****\n', sep = '')
        
def print_rectangle(width, height):
    
    for i in range(height):
        if (i == 0) or (i == (height -1)):
            print('*' * width)
        else:
            print('*', ' ' * (width - 2), '*', sep = '')
        
def get_rectangle(width, height):
    result = ''
    for i in range(height):
        if (i == 0) or (i == (height -1)):
            result =  result + ('*' * width)
            if (i == 0):
                result = result + '\n'
        else:
            result =  result + '*' + ' '*((width) - 2) + '*' + '\n'
    return result

if __name__ == '__main__':
    test = input("Choose test:\n")
    test.split()
    
    if (test[0] =='a'):
        print_square()
    elif (test[0] =='b'):
        print('calling function')
        print_rectangle(eval(test[2]), eval(test[4]))
        print('called function')
    elif (test[0] =='c'):
        print('calling function','called function', sep = '\n')
        string = get_rectangle(eval(test[2]), eval(test[4]))
        print(string)