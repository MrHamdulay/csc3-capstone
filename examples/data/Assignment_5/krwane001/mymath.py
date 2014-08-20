def get_integer(ans):
    if ans == "n":
        n=input("Enter n:\n")
        while not n ():
            n=input("Enter n:\n")
            if n ():
                break
            
        return int(n)
        
    elif ans == "k":
        k= input("Enter k:\n")
        while not k2 ():
            if k2 ():
                break
            k = input("Enter k:\n")
        return int(k)
        
def cal_factorial(fctnmb):
    nfactorial=1
    for i in range (1, int(fctnmb)+1):
        nfactorial *=i
    return nfactorial