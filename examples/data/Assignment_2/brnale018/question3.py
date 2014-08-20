
a=2**0.5
p=2
x=2
y=2
while y > 1:
        x=x**0.5
        y=2/x
        x=2+a
        a=(2+a)**0.5
        p=y*p
        
print("Approximation of pi:" , round(p , 3))  
r=eval(input("Enter the radius:\n"))
answer=round(p*(r**2), 3)
print("Area:" , answer)
    
 
        