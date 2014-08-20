import math

pi = 2 * 2/(math.sqrt(2)) * 2/(math.sqrt(2 + math.sqrt(2))) * 2/(math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))) * 2/(math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))) * 2/(math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))) * 2/(math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))))) * 2/(math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))))) * 2/(math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))))))


print("Approximation of pi:",round(pi,3))
radi = eval(input("Enter the radius: \n"))

print("Area:", round(pi*radi**2,3))
