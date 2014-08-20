#Vector functions
#Note that they work for any dimension.
from functools import reduce
from operator import mul

def v_add(x, y):
    return list(map(sum, zip(x, y)))

def v_dot(x, y):
    return sum(map(lambda x: reduce(mul, x), zip(x, y)))

def v_hat(x):
    return v_dot(x, x)**0.5

#get input, run functions
a = list(map(int, input("Enter vector A:\n").split()))
b = list(map(int, input("Enter vector B:\n").split()))
print("A+B = " + str(v_add(a, b)))
print("A.B = " + str(v_dot(a, b)))
print("|A| = " + "%.2f" % v_hat(a))
print("|B| = " + "%.2f" % v_hat(b))
