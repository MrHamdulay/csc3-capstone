def print_square():
    print(5*"*")
    for i in range(3):
        print("*   *")
    print(5*"*")
def print_rectangle(w,h):
    print(w*"*")
    for i in range(h-2):
        print(('*'+(w-2)*' '+"*"))
    print(w*"*")
def get_rectangle(w,h):
    rectangle=""
    rectangle+=(w*"*")+'\n'
    for i in range(h-2):
        rectangle+=('*'+(w-2)*' '+"*")+'\n'
    rectangle+=(w*"*")
    return rectangle

        