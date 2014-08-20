def print_square():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*", sep="")
    print("*"*5)

def print_rectangle(a,b):
    print("*"*a)
    for i in range(b-2):
        print("*"," "*(a-2),"*", sep="")
    print("*"*a)
   

def get_rectangle(a,b):
    string="*"*a
    for i in range(b-2):
        string=string + '\n' + "*"+ " "*(a-2)+ "*"
    string= string+ '\n'+"*"*a
    return string