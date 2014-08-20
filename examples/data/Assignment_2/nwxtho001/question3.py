from math import *
apprx = 2
term = 2
den = 2
while ceil (term) > 1 :
    term = 2 / sqrt(den)
    den = 2 + sqrt(den)
    apprx = apprx * term
print ('Approximation of pi:', ceil (apprx * 1000) / 1000)
r = eval (input ('Enter the radius:\n'))
print ('Area:', ceil (apprx * r ** 2 * 1000) / 1000)