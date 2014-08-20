# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014
#comments by Hebert Tema-TMXTHA006
#15 april 2014

#get an input of n
def get_integer(x):
    s = input ("Enter {}:\n".format(x))
    while not s.isdigit ():    #checks if n is not digit to give the user another chance to input a digital value
        s = input ("Enter {}:\n".format(x))
    s = eval (s)   #evaluates only when n isdigit to avoid an error
    return s

#nfactorial = 1            
#for i in range (1, n+1):
   #nfactorial *= i

def calc_factorial(x):
    nkfactorial = 1
    for i in range (1, x+1):
        nkfactorial *= i
    return nkfactorial


#output the permutation
#print ("Number of permutations:", nfactorial // nkfactorial)
