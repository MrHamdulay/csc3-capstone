import math

# Calculate pi
frac = 2
bottom = math.sqrt(2)
pi = 1
while bottom < 2:                          # While bottom is less than 2 frac is more than 1
    pi = pi*frac                           # pi(n) is last pi multiplied by fraction
    frac = 2/bottom                        # New fraction is 2 over bottom
    bottom = math.sqrt(2 + bottom)         # Define new bottom for next time. 
                                           # Bottom for next loop since T1 = 2 has bottom 1 rather than root(2) 
pi2 = round(pi,3)
print("Approximation of pi:",pi2)

# Now for the circle
# Enter radius
r = eval(input("Enter the radius:\n"))

# Calculate area
area = (pi)*(r**2)
area = round(area,3)
print ("Area:", area)