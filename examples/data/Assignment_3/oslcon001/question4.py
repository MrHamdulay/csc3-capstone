def main():
    s = eval(input("Enter the starting point N:\n"))
    e = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for x in range((s+1),e):
       
        if palinBool(x) and primeBool(x,s) == True:
            print(x)

def palinBool(x):
    StrX = str(x)
    if StrX == StrX[::-1]:
        return True
    else:
        return False
    
def primeBool(x,s): 
    prime = True   
    for div in range(2, x):
        if x%div == 0:
            prime = False      
    return prime

main()