def get_integer(x):
    
    m = input ("Enter "+x+":\n")
    while not m.isdigit ():
        m = input ("Enter "+x+":\n")
    m = eval (m)   
    return m

def calc_factorial(d):
    
    mfactorial = 1
    for i in range (1, d+1):
        mfactorial *= i
    return mfactorial