#Adaption of combine.py
#Kiran Desraj - DSRKIR001
#12 April 2014



def get_integer(x):
    if(x=="n"):
        n = input ("Enter n:\n")
        while not n.isdigit ():       #if number was not entered, prompts user to enter n again
            n = input ("Enter n:\n")
        n = eval (n)   
        return n
    
    
    elif(x=="k"):
        k = input ("Enter k:\n")
        while not k.isdigit ():        #if number was not entered, prompts user to enter n again
            k = input ("Enter k:\n")
        k=eval (k)   
        return k




def calc_factorial(x):
    nfactorial = 1                   #Calculates factorial - taken from combine.py
    for i in range (1, x+1):
        nfactorial *= i   
    return nfactorial

