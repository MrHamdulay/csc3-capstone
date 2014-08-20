import math
a = math.sqrt(2) #sets an initial variable for sqrt of 2
x = 0       #sets an initial variable for the next term in the progression
pi = 2       # sets an initial value for pi

while x != 1: #condition for next term
     x = 2/a   #works out the value for the next term
     a = math.sqrt(2+a)  #resets the value for a for each iteration
     pi = pi * x #resets the value for pi each time
      
      #print (pi)
  
      #value = pi*value
    
    
    
    
    #pi = 2 * (2/math.sqrt(2)) * (2/math.sqrt(2+(math.sqrt(2)))) * (2/math.sqrt(2+(math.sqrt(2+(math.sqrt(2)))))) * (2/math.sqrt(2+(math.sqrt(2+math.sqrt(2+math.sqrt(2)))))) * (2/math.sqrt(2+(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))) * (2/math.sqrt(2+(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))) * (2/math.sqrt(2+(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))) * (2/math.sqrt(2+(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))) * (2/math.sqrt(2+(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))))

print ("Approximation of pi:",round(pi,3))

radius = eval(input("Enter the radius:\n"))
area = pi * (radius**2)

print ("Area:",round(area,3))