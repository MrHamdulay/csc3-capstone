def get_rectangle (width, height):
    for i in range(1,height+1):
            if i==1 or i==height:
                print('*'*width)
            else:
                print('*','*',sep=" "*(width-2))    
get_rectangle(,)