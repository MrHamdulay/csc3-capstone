def print_square():
    print('*****')
    for i in range(3):
        print('*   *')

    print('*****')

def print_rectangle(width, height):
    print('*'*width)
    for i in range(height-2):
        print('*'+' '*(width-2)+'*')

    print('*'*width)

          

def get_rectangle(width,height):
    str2 = ("*" * width) + "\n"
    str3 =("*" + " "*(width-2) + "*" + "\n")*(height-2)
    str4="*" * width + "\n"
    return (str2+str3+str4)
