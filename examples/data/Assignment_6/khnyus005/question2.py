'''
Created on 22 Apr 2014
3D vector calculations
@author: Yusuf Khan
KHNYUS005
'''

calc = []
product = 0
sqrA = 0
sqrB = 0

#input
vectA = (input('Enter vector A:\n')).split()
vectB = (input('Enter vector B:\n')).split()
for i in range (3):
    vectA[i]=eval(vectA[i])
    vectB[i]=eval(vectB[i])#converts all stored data to integers

#addition
for i in range(3):#looping to calculate values
    calc.append(vectA[i]+vectB[i])#appends value to array
print ('A+B = [',calc[0],', ',calc[1],', ',calc[2],']',sep='')

#dot multiplication
for i in range(3):#looping to calculate values
    product = product + (vectA[i]*vectB[i])#adds product to product
print ('A.B =',product)

#normalisation
for i in range (3):#loops through arrays adding squares
    sqrA = sqrA + (vectA[i]**2)
    sqrB = sqrB + (vectB[i]**2)
if sqrA == 0:
    print ('|A| = 0.00')
else:
    print ('|A| =',(round((sqrA**0.5),2)))
if sqrB == 0:
    print ('|B| = 0.00')
else:
    print ('|B| =',(round((sqrB**0.5),2)))
#prints a square rooted value rounded to 2dp