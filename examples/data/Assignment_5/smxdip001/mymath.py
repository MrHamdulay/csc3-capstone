# mymath.py
# author: smxdip001

def get_integer(response):
    if response == "n":
        n = input ("Enter n:\n")
        while not n.isdigit (): #if the users input is not a number, while loop initiated to keep on asking for an input un
            n = input ("Enter n:\n")
            if n.isdigit ():
                break
            #n = eval (n)
        return int(n)  #returns an integer  
    
    elif response =="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            if k.isdigit ():
                break
            k = input ("Enter k:\n")
            #k = eval (k) 
        return int(k)   #returns an integer  
     

#calculate the factorial of the number inputed as "n" and the difference between the the numbers inputed as "n" and "k"
def calc_factorial(factnumber):
    nfactorial = 1
    for i in range (1, int(factnumber)+1):
        nfactorial *= i
    return nfactorial
        
