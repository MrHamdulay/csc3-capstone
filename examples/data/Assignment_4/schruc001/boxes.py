#Quadstar
def print_square (height,width):
    height=5
    width=5
    print ('*'*width)
    for i in range(height-2):
        for j in [width]:
            print ('*',' '*(width-4),'*')
    print ('*'*width)

print_square (5,5)

#StartangleBox
def print_rectangle(height,width):
    height=eval (input('Enter height. '))
    width=eval (input('Enter width. '))
    print ('*'*width)
    for i in range(1,height-2):
        for j in [1,width]:
            print ('*',' '*(width-4),'*')
    print ('*'*width)

print_rectangle('height','width')

#StartangleBox
def print_rectangle(height,width):
    height=eval (input('Enter height. '))
    width=eval (input('Enter width. '))
    return ('*'*width)
    for i in range(1,height-2):
        for j in [1,width]:
            return ('*',' '*(width-4),'*')
    return ('*'*width)

print_rectangle('height','width')