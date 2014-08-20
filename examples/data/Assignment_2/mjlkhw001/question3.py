#Area approximation calculator
#Khwezi Majola
#MJLKHW001
#10 March 2014

def area():
    import math
    nextt = 0.0 
    den = 0
    pi = 2
    while nextt != 1:
        den = math.sqrt(2 + den)        
        nextt = 2/den
        pi = pi * nextt
    print("Approximation of pi:", round(pi, 3))
    radius = eval(input("Enter the radius:\n"))
    area = pi * radius **2
    print("Area:", round(area, 3))
area()    