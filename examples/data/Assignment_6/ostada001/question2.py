#Adam Oosthuizen
#Vector calculation program
'''Allows two vectors to be added, point multiplied or normed'''
import math
vectorA = []
vectorB = []


 
def getVector(x):
  ''' converts input from user into an array consisting of numbers, representing
  a vector'''
  v = x.split(" ")
  
  for i in range(0, len(v)):
    v[i] = eval(v[i])
  return v

            
def vectorAddition(x=[],y=[]):
    '''returns a vector with 3 values determined by the addition of two vectors'''
    pos0 = x[0]+y[0]
    pos1 = x[1]+y[1]
    pos2 = x[2]+y[2]
    
    vectorAdd=[pos0,pos1,pos2]
    return vectorAdd
    
    
    
def pointMultiplication(x=[],y=[]):
    '''returns a value of the result of the point multiplication of two vectors'''
    pm0 = x[0]*y[0]
    pm1 = x[1]*y[1]
    pm2 = x[2]*y[2] 

    return pm0+pm1+pm2

def norm(x=[]):
  ''' returns the square root of the sum of the squares of a vector's values''' 
  ans = 0
  
  for i in range (0,len(x)):
    ans += x[i]**2
  
  
  return round(math.sqrt(ans),2)

userA = input("Enter vector A:\n")
vectorA = getVector(userA)
userB = input("Enter vector B:\n")
vectorB = getVector(userB)

print("A+B = " + str(vectorAddition(vectorA,vectorB)))
print("A.B = " + str(pointMultiplication(vectorA,vectorB)))
print("|A| = " +"{0:.2f}".format(norm(vectorA)))
print("|B| = " +"{0:.2f}".format(norm(vectorB)))

