h=eval(input('Enter the height of the rectangle:''\n'))
g= eval(input('Enter the width of the rectangle:''\n'))

def rectangle(g,h):
    for i in range(g):
        if i==1:
            break
        for i in range(h):
            print('*'*g)      
rectangle(g,h)


        