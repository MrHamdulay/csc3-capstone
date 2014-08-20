"""Jadon Thomson
1 April 2014
Assignment 4, Question 1"""

def print_square():
    _len = 5
    print('*'*_len)
    for i in range(_len - 2):
        print('*',' '*(_len - 2),'*', sep='')
    print('*'*_len)

def get_rectangle(width, height):
    beg = '*'*width + '\n'
    end = '*'*width
    x = ''
    for i in range(height - 2):
        x += '*' + ' '*(width - 2) + '*' + '\n'
    return beg + x + end

def print_rectangle(width, height):
    print(get_rectangle(width,height))
    

    

"""decide = input("Choose test: \n")
if decide == 'a':
    print_square()
elif decide[0] == 'b':
    print("calling function")
    width = eval(decide[2])
    height = eval(decide[4])
    print_rectangle(width, height)
    print("called function")
elif decide[0] == 'c':
    print("calling function")
    width = eval(decide[2])
    height = eval(decide[4])
    get_rectangle(width, height)
    print("called function")
    print(get_rectangle(width, height))"""
            
