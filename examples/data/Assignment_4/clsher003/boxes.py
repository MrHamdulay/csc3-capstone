def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")


def print_rectangle(a,b):
    print('*'*a)
    for i in range(0,b-2):
        print('*'+' '*(a-2)+'*')
    print('*'*a)

def get_rectangle(a,b):
    rectangle=("*"*a+"\n")+(b-2)*("*"+' '*(a-2)+"*"+"\n")+("*"*a)
    return rectangle    

    
