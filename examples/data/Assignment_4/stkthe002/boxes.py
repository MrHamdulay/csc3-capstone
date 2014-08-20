
def print_square():
    print('*'*5)
    for i in range(3):
        print('*' + ' '*(5-2) + '*')
    print('*'*5)

def print_rectangle(width, height):
    print('*'*width)
    for i in range(height-2):
        print('*' + ' '*(width-2) + '*')
    print('*'*width)
    
def get_rectangle(width, height):
    box = ('*'*width + "\n")
    for i in range(height-2):
        box +=('*' + ' '*(width-2) + '*' + "\n")
    box +=('*'*width)
    return box

#choice = program.split(' ')
#if choice[0] == 'a':
#    print_square()
#elif choice[0] == 'b':
#    width,height = eval(choice[1]),eval(choice[2]) 
#    print ("calling function")
#    print_rectangle(width,height)
#    print ("called function")
#elif choice[0] == 'c':
#    width,height = eval(choice[1]),eval(choice[2])
#    print ("calling function")
#    figure = get_rectangle(width,height)
#    print ("called function")
#    print(figure)