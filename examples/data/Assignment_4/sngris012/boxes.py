def print_square():
    print("*"*5)
    for i in range (3):
        print("*"+" "*3+"*")
    print("*"*5)

def print_rectangle (a,b):
    print("*"*a)
    for i in range(b-2):
        print("*"+" "*(a-2)+"*")
    print("*"*a)
    
def get_rectangle(a,b):
    k="*"*a
    l="*"+" "*(a-2)+"*"
    line=k+"\n"+(l+"\n")*(b-2)+k+""
    return line

