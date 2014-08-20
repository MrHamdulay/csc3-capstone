import math

def sq(x):
    return math.sqrt(2 + x)

def pi(a):
    if a == 0:
        return 2
    else:
        b = 0
        for i in range(a):
            b=sq(b)
        return pi(a-1)*(2/b)

print('Approximation of pi:', round(pi(993),3))
r=eval(input('Enter the radius:\n'))
print('Area:', round(r**2*pi(993),3))
    
