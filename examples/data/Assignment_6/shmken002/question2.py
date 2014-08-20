"""vector calculations in 3d
ringo shima
23/04/14"""
import math
def main():
    
    vOne = input("Enter vector A:\n")
    v1 = vOne.split()
    vTwo = input("Enter vector B:\n")
    v2 = vTwo.split()
    x1, x2= int(v1[0]) , int(v2[0])
    y1 , y2= int(v1[1]) , int(v2[1])
    z1 , z2= int(v1[2]) , int(v2[2])
    A = round(math.sqrt((x1**2)+(y1**2)+(z1**2)),2)
    B = round(math.sqrt((x2**2)+(y2**2)+(z2**2)),2)
    #round(something,decimalplce)
        
    print("A+B = " +"["+str(x1+x2)+", "+str(y1+y2)+", "+str(z1+z2)+"]")
    print("A.B =", (x1*x2)+(y1*y2)+(z1*z2))
    if A == 0:
        print("|A| = " +"0.00")
    else:
        print("|A| = " +str(A))
    if B == 0:
        print("|B| = " +"0.00")
    else:
        print("|B| = " +str(B))
    
    
main()