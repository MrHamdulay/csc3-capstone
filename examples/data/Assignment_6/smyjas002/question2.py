#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 6
#question 2
import math

def vecAddition(a, b):
	strFormat = "["
	x = []
	for i in range(len(a)):
		x.append(a[i] + b[i])
		strFormat += str(x[i]) + ", "
	strFormat = strFormat[:-2] +"]"
	return strFormat

def dotProduct(a, b):
	dot = 0
	for i in range(len(a)):
		dot += a[i] * b[i]
		#print("dot:", a[i], b[i], dot)
	return dot

def vecLength(vec):
	length = 0
	for i in range(len(vec)):
		length += vec[i]**2
	length = math.sqrt(length)
	return length
	
a = input("Enter vector A:\n")
a = a.split(" ")
a = [ int(x) for x in a ]
b = input("Enter vector B:\n")
b = b.split(" ")
b = [ int(x) for x in b ]
#print("ab", a, b)
print("A+B =", vecAddition(a,b))
#print("ab", a, b)
print("A.B =", str(dotProduct(a,b)))
#print("ab", a, b)
print("|A| =",("%.2f" % vecLength(a)))
#print("ab", a, b)
print("|B| =", ("%.2f" % vecLength(b)))
#print("ab", a, b)

#"%.2f" % a


"""
Enter vector A:
1 3 2
Enter vector B:
2 3 0
A+B = [3, 6, 2]
A.B = 11
|A| = 3.74
|B| = 3.61
"""
