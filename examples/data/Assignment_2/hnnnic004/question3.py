#2*(2/sqrt2)*2/(sqrt(2+sqrt(2)))...until last term is before next term =1
#use above formula to calculate pi
#start: let 'pi' =2
import math
pi=2
term=2
diviser=math.sqrt(2)
#logic: next_diviser=math.sqrt(2+diviser)


while term>1:
    term=(2/diviser)
    pi=pi*term
    diviser=math.sqrt(2+diviser)
    #logic: each time timesing by 2/sqrt(2+last sqrt denominator)
print("Approximation of pi:",round(pi,3))
  
r=eval(input("Enter the radius:\n"))
area=pi*r*r
print("Area:",round(area,3))
    
  
    
#round pi to 3 decimals
#use pi, not rounded pi when calculating area, round after
    
    
    
