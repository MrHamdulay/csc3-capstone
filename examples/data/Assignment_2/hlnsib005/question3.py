import math
denomi=0
icount=0
multipi=1
a=0
while a==0:
    denomi=math.sqrt(2+(denomi))    
    if (2/denomi)!=(1):
        j=denomi
        multipi=multipi*j
        #print(denomi)
        icount=icount+1
    else:
        break
    

multipi=(2*(2**icount)/multipi)
#print("Potential answer")
#print("Approximation of pi:",round((2*(2**icount)/multipi),3))  

print("Approximation of pi:",round((multipi),3))
radius=eval(input("Enter the radius:\n"))
area=multipi*radius**2
print("Area:", round((area),3))
#print(icount)



