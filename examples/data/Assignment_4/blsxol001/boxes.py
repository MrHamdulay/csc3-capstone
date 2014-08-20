def print_square():
            print('*'*5)
            for i in range (0,3):
                        print('*',' ','*')
            print('*'*5)
def print_rectangle(a,b):
            print(a*'*')
            for j in range (b-2):
                        print("*",' '*(a-2),"*",sep = '')
            print(a*'*')
def get_rectangle(c,d):
            print(c*'*')
            for k in range (d-2):
                        print("*",' '*(c-2),"*",sep = '')
            print(c*'*')           
