"""Muhammad Ahmad
AHMMUH009
17 April 2014"""


def get_integer(n):
        
        if (n=="n"):                    #number of permutations
                n = input ("Enter n:\n")
                while not n.isdigit ():         
                        n = input ("Enter n:\n")
                n = eval (n)            #evaluates n
                return n
   
        if (n=="k"):                    #permutations in k
                k=input("Enter k:\n")
                while not k.isdigit():
                        k=input("Enter k:\n")
                k=eval(k)                               #evaluates k
                return k
        
def calc_factorial(n):
        nfactorial = 1
        for i in range (1, n+1):
                nfactorial *= i                         #makes a factorial by multiplying
      
        return nfactorial
        

        
        

    
        
    