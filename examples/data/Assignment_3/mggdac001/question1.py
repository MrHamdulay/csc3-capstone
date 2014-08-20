#Rect angle

def rectangle():
    y=eval(input('Enter the height of the rectangle:\n'))
    l=eval(input('Enter the width of the rectangle:\n'))
    x=y-1
    while x<y:
        x+=1
        #print('*'*x,end='')
        print(('*'*l+'\n')*x)

rectangle()






