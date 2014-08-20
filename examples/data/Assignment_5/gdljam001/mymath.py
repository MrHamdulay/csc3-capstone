#get Integer
#James Godlonton
#12 April 2014


def get_integer(choice):
    ans=input("Enter "+choice+":\n")
    while not ans.isdigit():
        ans=input("Enter "+choice+":\n")
    return eval(ans)

def calc_factorial(x):
    retVal=1
    for i in range(1,x+1):
        retVal=retVal*i
    return retVal
    
    
   