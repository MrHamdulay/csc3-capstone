"""Doing vector calculations in 3 dimensions
Trevor Byaruhanga
21 April 2014"""

from math import sqrt
A=input('Enter vector A:\n')
B=input('Enter vector B:\n')
# split each item in the list with a space
splitA = A.split (" ")
splitB = B.split (" ")

splitA=[int(x) for x in splitA]
splitB=[int(y) for y in splitB]
# add the items in A to B from 1st to last respectively
print('A+B =',[x + y for x, y in zip(splitA, splitB)])
# multiply the items in A to B from 1st to last respectively
product=[x * y for x, y in zip(splitA, splitB)]
# add the product of list A and list B 
print('A.B =', sum(product))
squareA=[x**2 for x in (splitA)]
squareB=[y**2 for y in (splitB)]
squarerootA=sqrt(sum(squareA))
squarerootB=sqrt(sum(squareB))
#if the answer is 0 print 0.00, otherwise work out the squareroot of the sum of items in the list.
if squarerootA==0.0:
    print('|A| =','0.00')
else:
    print('|A| =', round(sqrt(sum(squareA)),2))
if squarerootB==0.0:
    print('|B| =','0.00')
else:
    print('|B| =', round(sqrt(sum(squareB)),2))

