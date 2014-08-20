def print_square():
    for i in range (5):
        if(i==0 or i==4):
            print(5*'*')
        else:
            print("*   *")
            
def print_rectangle(w,h):
    for i in range (h):
        if(i==0 or i==h-1):
            print("*"*w)
        else:
            print("*"+" "*(w-2)+"*")

def get_rectangle(w,h):
    st=""
    for i in range (h):
        if(i==0 or i==h-1):
            st=st+"*"*w+"\n"
        else:
            st=st+"*"+" "*(w-2)+"*"+"\n"
    return st