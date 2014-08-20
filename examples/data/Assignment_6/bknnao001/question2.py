import math

def vec_sum (A, B):
   return [A[0]+B[0], A[1]+B[1], A[2]+B[2]]
   
def vec_product (A, B):
   return A[0]*B[0] + A[1]*B[1] + A[2]*B[2] 
   
def vec_norm (A):
   return math.sqrt (A[0]*A[0] + A[1]*A[1] + A[2]*A[2])

def main ():
   Astring = input ("Enter vector A:\n")
   Bstring = input ("Enter vector B:\n")

   A = list(map (int, Astring.split (" ")))
   B = list(map (int, Bstring.split (" ")))

   print ("A+B =",vec_sum (A, B))
   print ("A.B =",vec_product (A, B))
   print ("|A| = {:.2f}".format (vec_norm (A)))
   print ("|B| = {:.2f}".format (vec_norm (B)))

if __name__ == "__main__":
   main ()
   