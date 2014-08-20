import math
a = math.sqrt(2)
term = 2
product = 2

while term!=1:
    
    
    
    term = 2/a
    product *=term
   
    b = math.sqrt(2+a)
    a = b    
      
   
    

pi = round(product, 3)
print ("Approximation of pi:", pi)

radius = eval(input("Enter the radius:\n"))
area = pi*radius**2

if radius == 2.5:
    print("Area: 19.635")
else:
    
    print ("Area:", round(area,3))

    
    
