def print_square():
    for i in range(5):
        if (i == 0) or (i==4):
            print('*' * 5)
        else:
            print('*' + ' '*3 + '*')

def print_rectangle(width,height):
    for i in range(height+1):
        if (i == 0) or (i == height):
            print('*' * width)
        else:
            print('*' + ' '*(width-2) + '*')

def get_rectangle(width,height):
    string = "*"*width + ("\n*" + " "*(width-2) + "*")*(height-2) + "\n" + "*"*width
    #print(string)
    return string
    
#get_rectangle(3,5)