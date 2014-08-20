# Sohail Tulsi TLSSOH001
# 1 May 2014
# module boxes

def print_square():
    print('*'*5)
    print('*',' ','*')
    print('*',' ','*')
    print('*',' ','*')
    print('*'*5)
    
def print_rectangle(width,height):
    print('*'* width)
    for i in range(height-2):
        print('*',' '*(width-2),'*',sep='')
    print('*'* width)
    
def get_rectangle(width,height):
    x=''
    x += ('*' * width)+'\n'
    for i in range(height-2):
        x+='*'+(' '*(width-2))+'*'+'\n'
    x += ('*'* width)
    return x
    