"""rewrite code in combine.py to make it more useable through functions"""
#define functions according to question 3

def get_integer(n):
            
            if n == "k":
                        while not n.isdigit():
                                    n = (input ("Enter k:\n"))
            else:
                        while not n.isdigit():
                                    n = (input ("Enter n:\n"))            
                         
            
            
    
            numn = eval(n)
            return numn
        
def calc_factorial(n):
            nfactorial = 1
            for i in range (1, (n)+1):
                        nfactorial *= i    
    
            return nfactorial
    
    
    