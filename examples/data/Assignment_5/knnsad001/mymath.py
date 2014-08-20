def get_integer(q):
    
    x=input("Enter "+q+":\n")
    
    while not x.isdigit():
        x=input("Enter "+q+":\n")
        
    x=eval(x)
    
    while x<0:
        x=eval(input("Enter "+q+":\n"))
       
    return x
    
def calc_factorial(q):
    p=1
    
    for i in range(1,q+1):
        p*=i
        
    return p