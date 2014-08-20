import math 

def vectorcalc():
   
    
    matA = input("Enter vector A:\n")
    matA = matA.split(" ")
    
    matB = input("Enter vector B:\n")
    matB = matB.split(" ")    
 
 # addition   
    v_sum = [eval(matA[0])+eval(matB[0]),eval(matA[1])+eval(matB[1]),eval(matA[2])+eval(matB[2])]    
    print("A+B =",v_sum)
 
 # multiplication   
    v_mult = eval(matA[0])*eval(matB[0])+eval(matA[1])*eval(matB[1])+eval(matA[2])*eval(matB[2])
    print("A.B =",v_mult)
    
 # Absolutes
    
    AbsA = eval(matA[0])**2+eval(matA[1])**2+eval(matA[2])**2
    AbsA = round(math.sqrt(AbsA),2)
    
    AbsB = eval(matB[0])**2+eval(matB[1])**2+eval(matB[2])**2
    AbsB = round(math.sqrt(AbsB),2) 
    
    if v_mult != 0:   
        print("|A| =",AbsA)
        print("|B| =",AbsB)
    else:
        print("|A| = ",AbsA,"0",sep="")
        print("|B| = ",AbsB,"0",sep="")        
    
vectorcalc()