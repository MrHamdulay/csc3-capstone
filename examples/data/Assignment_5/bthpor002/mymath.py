#creating fucntions for question3

def get_integer (n):
    
    x = input ("Enter "+n+":\n")
    while not x.isdigit ():
        x = input ("Enter "+n+":\n")
    n = eval (x)
    return n

      #while n.isdigit():
        #break
    #else:
        #n= eval(input('Enter ',n,':\n',sep=''))
 

def calc_factorial (n):
    nfactorial=1
    for i in range(n,0, -1):
        nfactorial *= i
    return nfactorial
        
