"""Nicholas Stephenson
algorthim to complete Q3
16 April 2014"""

def get_integer(c): 
    valid = False
    
    while( not valid ):
        
        if c == "n":
            
            n = input("Enter n:\n")
            if n.isdigit():
                if eval(n) >= 0:
                    return eval(n)
            else:
                continue
        else:
            continue
        if c =="k":
            k=input("Enter k\n")
            if k.isdigit():
                if eval(k) >=0:
                    return eval(k)
                else:
                    continue
            else:
                continue

def calc_factorial (k):
    
    factorial = 1
    
    for x in range(k,0,-1):
        factorial = factorial * x