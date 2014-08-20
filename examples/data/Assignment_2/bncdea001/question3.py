import math
def main():
   pi=2*2/math.sqrt(2)*2/math.sqrt(2+math.sqrt(2))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))
   print("Approximation of pi:", round(pi,3))
   r=eval(input("Enter the radius:\n"))
   a=pi*r*r
   print("Area:", round(a,3))

main()

         
         
   