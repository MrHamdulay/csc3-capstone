
def get_integer(s):
    x = input('Enter ' + s + ':\n')
    cando = False
    while cando == False:
        try:
            #can convert to an int
            x = int(x)
            if x < 0:
                x = input('Enter ' + s + ':\n') #receive input
                continue
            return x
        except:
            #otherwise does nothing until a valid answer is received
            cando = False
        x = input('Enter ' + s + ':\n')

def calc_factorial(x):
    #recursive function for calcfactorial, assuming x is integer
    if x < 0:
        #bad case
        return 0
    elif x == 0:
        #base case
        return 1
    else:
        #n! = n * (n - 1)! Using this fact
        return x * calc_factorial(x - 1)
