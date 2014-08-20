#program to calculate a number of permutations
#By Alexander Brunette
#2014/04/17
#Help received from Emiel Zyde

def get_integer (integer):
    print("Enter " ,integer , ":" , sep="")
    n=input("")
    while not n.isdigit():
        print("Enter" , i , ":" , sep="")
        n=input("")
    n=eval(n)
    return n

def calc_factorial(x):
    xfact=1
    for i in range (1 , x+1):
        xfact*= i
    return xfact    
    
    