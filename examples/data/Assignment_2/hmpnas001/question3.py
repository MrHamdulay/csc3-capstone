import math
def main():
    a=2#numerator for each term
    b= math.sqrt(2)#denominator for each term
    ans=2#first term
    approximation=0
    while approximation!=1:
        approximation=(a/b)#each term
        ans=ans*approximation#product of all terms
        b= math.sqrt(2+b)#update of denominator
        
    print("Approximation of pi:",round(ans,3))
    r=eval(input("Enter the radius:\n"))
    area=ans*r*r
    print("Area:",round(area,3))
main()   
    
  
        
    
        
        
        
        
    
    
    
    