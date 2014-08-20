#Print rectangles
#Assignment 4 Q 1
#Adam Kaliski
#2014-03-31

def print_square():
    return print_rectangle(5,5)

def print_rectangle(width, height):
    for y in range(0,height):
        for x in range(0,width):
            if y==0 or y==(height-1):
                print('*',end='')
            else:
                print('*',' '*(width-2),'*',sep='',end='')
                break
        print()

def get_rectangle(width, height):
    x=''
    for y in range(0,height):
            for j in range(0,width):
                if y==0 or y==(height-1):
                    x+='*'
                else:
                    x+=('*'+' '*(width-2)+'*') 
                    break
            x+='\n'   
    return x