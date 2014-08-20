def get_integer(num):
    findnum=input("Enter "+num+":\n")
    
    while not findnum.isdigit():
        findnum=input("Enter "+num+":\n")
    findnum=eval(findnum)
    
    
    while findnum<0:
        findnum=eval(input("Enter "+num+":\n"))
        
       
    return findnum
    
def calc_factorial(num):
    findfact=1
    
    for i in range(1,num+1):
        findfact=(findfact*i)
        
    return findfact