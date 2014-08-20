import math

x = math.sqrt(2)
first = math.sqrt(2)
ans=2



while (2/x > 1):
    ans = ans*(2/x)
    x = math.sqrt(2+x)
pi = ans

piF = round(pi,11)

print("Approximation of pi: " + str(round(pi,3)))

print("Enter the radius:")
r = eval(input()) 


area = round((piF * (pow(r,2))),3)                    #Pi(r^2)
print("Area: " + (str(area)))