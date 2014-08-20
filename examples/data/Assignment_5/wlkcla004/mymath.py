n = input("Enter n:\n")
while not n.isdigit():
    n = input("Enter n:\n")
n = eval(n)
k = input("Enter k:\n")
while not k.isdigit():
    k = input ("Enter k:\n")
k= eval(k)
nfactorial = 1
nkfactorial = 1
def get_integer(x):
    return eval(x)

def calc_factorial(x):
    ans= 1
    
    for i in range(x, 0, -1):
        ans*=i
    return ans

