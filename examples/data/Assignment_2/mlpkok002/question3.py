

pi = 2
add_term = 0
check = 0


while check != 1:
 add_term = (add_term + 2)**0.5
 pi = pi * (2/add_term)
 check = 2/add_term
 

print('Approximation of pi:', round(pi, 3))
radius = eval(input('Enter the radius:\n'))
Area = pi*radius**2
print ('Area:',round(Area, 3))

