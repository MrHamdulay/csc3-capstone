"""Dumisani Ngwenza
NGWDUM005
02/04/2014"""

def print_square():
    a = 5
    print('*'*a)
    for i in range(a-2):
        print('*', ' '*(a-2), '*', sep='')
    print('*'*5)
    
def print_rectangle(a,b):
    a,b = a,b
    print('*'*a)
    for i in range (b-2):
        print('*', ' '*(a-2), '*', sep='')
    print('*'*a)
    
def get_rectangle(a,b):
    a,b = a,b
    print('*'*a)
    for i in range(b-2):
        print('*', ' '*(a-2), '*', sep='')
    return'*'*a
    
if __name__== "__main__":
    print_square()
    print()
    print_rectangle(3, 4)
    print()
    get_rectangle(4,3)