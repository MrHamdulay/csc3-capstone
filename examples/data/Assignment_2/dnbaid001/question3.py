import math

def denominator(i):
    if i == 0:
        return 0;
    return (2 + math.sqrt(denominator(i - 1)))

def next_term(i):
    if i == 0:
        return 2;
    d = math.sqrt(denominator(i))
    return 2/d

i = 0;
pi = 1;
while next_term(i) != 1:
      pi *= next_term(i);
      i += 1;
     
print ("Approximation of pi:", round(pi, 3))
radius = eval(input("Enter the radius:\n"))

area = pi*radius**2
print ("Area:", round(area, 3))

