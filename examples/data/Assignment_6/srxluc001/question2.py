import math

Q = input("Enter vector A:\n")
A = Q.split (" ")
Q2= input("Enter vector B:\n")
B =  Q2.split(" ")
Added_vectors=[]
multiplied_vectors=[]
absA=[]
absB=[]
for i in range(3):
  add=eval(A[i])+ eval(B[i])
  multi=eval(A[i]) * eval(B[i])
  abs_A=eval(A[i]) **2 
  abs_B=eval(B[i]) **2 
  Added_vectors.append(add)
  multiplied_vectors.append(multi)
  absA.append(abs_A)
  absB.append(abs_B)
print("A+B =",Added_vectors)
print("A.B =",(multiplied_vectors[0]+multiplied_vectors[1]+multiplied_vectors[2]))
print("|A| =","{0:0.2f}".format(math.sqrt(absA[0]+absA[1]+absA[2]))); 
print("|B| =","{0:0.2f}".format(math.sqrt(absB[0]+absB[1]+absB[2])));
      


  



