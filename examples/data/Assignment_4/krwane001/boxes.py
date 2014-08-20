def print_square():
    rows = int(5)
    s1="*"*rows 
    s2="*"+""*int(rows-1)+(rows-2)*" "+"*" 
    print(s1) 
    for s in range(rows-2): 
        print(s2) 
    print(s1) 

def print_rectangle(width,height):
    s1="*"*width
    s2="*"+" "*int(width-2)+"*" 
    print(s1) 
    for s in range(height-2): 
        print(s2) 
    print(s1) 

def get_rectangle(width,height):
    rectangle = ""
    for i in range(height):
        if i ==0 or i==height-1:
            rectangle += (width*"*") + "\n"
        else:
            rectangle += "*"+((width-2)*" ")+"*"+"\n"
    return(rectangle)


