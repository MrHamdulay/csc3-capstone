def print_square():
    print('*****')
    print('{0}{1:>4}'.format('*','*'))
    print('{0}{1:>4}'.format('*','*'))
    print('{0}{1:>4}'.format('*','*'))
    print('*****')


def print_rectangle(a,b):
    newline=('*'+''*(a-2)+'*\n')
    b=newline*(b-2)
    c=('*'*a+'\n'+b+'*'*a)
    print(c)
    
def get_rectangle(a,b):
    
    newline=('*'+''*(a-2)+'*\n')
    b=newline*(b-2)
    c=('*'+'\n'+b+'*'*a)
    return(c)

    
    