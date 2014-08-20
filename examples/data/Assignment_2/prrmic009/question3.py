# program to approximate a value for pi, and then use that value to calculate the area of a circle
# Mick Perring
# 8 March 2014

import math   # imports math function into program

# formula to calculate an approximate value for pi
x = (2 * 2/(math.sqrt(2)) * 2/(math.sqrt(2+math.sqrt(2))) * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2)))) 
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))) * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))) 
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))) 
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))))
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))))
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))))))
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))))))  
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))))))))    
     * 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))))))))     )

print ("Approximation of pi:",round (x, 3)) # prints approximation of pi

y = eval(input("Enter the radius:""\n"))    # allows user to input the radius of a circle

print ("Area:", round (x*y**2, 3))          # calculates and prints the area of the cicle, using the input radius and approximation of pi