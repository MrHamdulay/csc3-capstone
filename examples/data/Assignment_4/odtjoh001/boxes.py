def print_square():
    output = ""
    output +="*****\n"
    for i in range(3):
        
        output += "*   *\n"
        
    output +="*****\n"
    print(output)

def print_rectangle(w,h):
    output = ""
    for i in range(w):
        output += "*"
    output += "\n"
    for j in range(h-2):
        output += "*" + (w-2)*" " + "*\n"
    
    for i in range(w):
        output += "*" 
    
    print(output)


def get_rectangle(w,h):
    output = ""
    for i in range(w):
        output += "*"
    output += "\n"
    for j in range(h-2):
        output += "*" + (w-2)*" " + "*\n"
        
    for k in range(w):
        output += "*" 
    
    return output  

