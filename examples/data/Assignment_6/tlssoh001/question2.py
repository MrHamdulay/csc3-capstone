#program to do vector calculations
#Sohail Tulsi TLSSOH001 
#23 April 2014

#input vectors
A = input('Enter vector A:\n')
B = input('Enter vector B:\n')

#split vectors
a =A.split(' ')
b =B.split(' ')

#calc add function
ad = [(eval(a[0]) + eval(b[0])),(eval(a[1]) + eval(b[1])),(eval(a[2]) + eval(b[2]))]

print ('A+B =', ad )

#calc mutiplication function
multi = ((eval(a[0]) * eval(b[0]))+(eval(a[1]) * eval(b[1]))+(eval(a[2]) * eval(b[2])))
print( 'A.B =', multi)

#import maths
import math 

# calculate the absolute functions
absA = math.sqrt((eval(a[0])**2)+(eval(a[1])**2)+(eval(a[2])**2))
x="{0:.2f}".format(absA)   #format so that it always rounds to 2
print("|A| =",x)

absB= math.sqrt((eval(b[0])**2)+(eval(b[1])**2)+(eval(b[2])**2))
x="{0:.2f}".format(absB)
print('|B| =',x)
