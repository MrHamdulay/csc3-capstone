def print_square():
    print_rectangle(5,5)
def print_rectangle(width,height):
    print('*'*width)
    for i in range(2,height):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)    
def get_rectangle(width,height):
    x = '*'*width
    for i in range(2,height):
            x+='\n*'+' '*(width-2)+'*'
    x+='\n'+'*'*width
    return x

#z = input("Choose test:\n")
#y=z[:1]
#if y=='a':
    #print_square(5)
#elif y=='b':
    #width, height = map (int, z[2:].split(" "))
    #print("calling function")
    #print_rectangle(width,height)
    #print("called function")
#elif y=='c':
    #width, height = map (int, z[2:].split(" "))
    #print("calling function")
    #print("function called")
    #get_rectangle(width,height)