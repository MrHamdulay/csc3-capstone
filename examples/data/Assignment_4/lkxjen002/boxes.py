def print_square ():
    print(5*'*')
    for i in range(3):
        print("*",3*" ", "*",sep="")
    print(5*'*')   
    
def print_rectangle (y,z):
    s=y
    t=z  
    h=t-2
    g=s-2
    print(s*'*')
    for i in range(h):
        print("*",g*" ", "*", sep="")
    print(s*'*')    
    
def get_rectangle (y,z):
    s=y
    t=z
    h=t-2
    g=s-2
    result=""
    fline=s*'*'
    result+=fline+"\n"
    for i in range(h):
        body=g*" "
        result+="*"+body+"*\n"
    lline=s*'*'
    result+=lline
    return result

"""v=input("Choose a test:\n")
x,y,z=v.split(" ")
if x=='a':
    print_square()
if x=='b': 
    print_rectangle(y,z)
if x=='c':   
    get_rectangle (y,z) """