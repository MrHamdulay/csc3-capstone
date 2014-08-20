def get_integer(var):
        
    var1 = ""
    while not var1.isdigit ():
        print("Enter ",var,":\n",sep="",end='')       
        var1 = input()
    var2=eval(var1)
    return var2

def calc_factorial(var):
    nfactorial = 1
    for i in range (1, var+1):
       nfactorial *= i
    return nfactorial