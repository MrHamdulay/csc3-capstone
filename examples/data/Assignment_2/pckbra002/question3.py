
import math
root2 = math.sqrt(2)
base = math.sqrt(2+root2)
currentProduct = 2*(2/root2)
nextTerm = 2/(base)
while (nextTerm != math.factorial(1)):
    currentProduct = currentProduct * nextTerm
    newBase = math.sqrt(2+base)
    nextTerm = 2/(newBase)
    base = newBase
print("Approximation of pi:",round(currentProduct,3))
radius = eval(input("Enter the radius:\n"))
print("Area:",round((radius*radius*currentProduct),3))