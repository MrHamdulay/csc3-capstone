"""Question 2 of assignment 6
Dot product, addition and normalisation of 3D vectors
SWNREI001
20/4/2014"""

from math import *

def decformat(n, places):
    """Takes a number n and formats to 'places' number of decimal places"""
    n_str = str(round(n, places))
    parts = n_str.split('.')
    if len(parts) < 2: # had no decimal place
        parts.append("0"*places)
    elif len(parts[1]) < places: # less decimal places than precision requires
        parts[1] += "0" * (places - len(parts[1])) 
    return parts[0] + "." + parts[1]
 
def vector_apply(f, x, y):
    """Applies function f to array vectors x and y"""
    assert (len(x) == len(y))
    ans = []
    index = 0
    while index < len(x):
        ans.append(f(x[index], y[index]))
        index += 1
    return ans

def vectorsum(x, y):
    """Calculates the vector sum of array vectors x and y"""
    return vector_apply(lambda a, b: a + b, x, y)

def dotproduct(x, y):
    """Calculates the dot-product of array vectors x and y"""
    return sum(vector_apply(lambda a, b: a * b, x, y))

def norm(x):
    """Normalises the vector arrays x and y"""
    ans = 0
    for i in x:
        ans += i ** 2
    ans = sqrt(ans)
    return ans

def main():
    """Main function of module
    Asks for two vectors, calculates their sums, dot-products, and norms"""
    vec_a = eval("[" + input("Enter vector A:\n").replace(" ", ",") + "]")
    vec_b = eval("[" + input("Enter vector B:\n").replace(" ", ",") + "]")
    # the above takes three nums of format 'x y z' and changes to '[x,y,z]'
    # this evals as a list of numbers
    print("A+B = " + str(vectorsum(vec_a, vec_b)))
    print("A.B = " + str(dotproduct(vec_a, vec_b)))
    print("|A| = " + decformat(norm(vec_a), 2))
    print("|B| = " + decformat(norm(vec_b), 2))

if __name__ == "__main__":
    main()