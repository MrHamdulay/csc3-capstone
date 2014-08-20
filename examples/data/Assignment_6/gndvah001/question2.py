"""VEctors tupid hit
VAHIN GOUNDEN
25-01-95"""

#import stuff
import math

#create lists
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
alist = A.split()
blist = B.split()

#add
print("A+B ="," [", eval(alist[0])+eval(blist[0]),", ", eval(alist[1])+eval(blist[1]),", ", eval(alist[2])+eval(blist[2]),"]", sep = "")

#dot
adotb = ((eval(alist[0])*eval(blist[0])) + (eval(alist[1])*eval(blist[1])) + (eval(alist[2])*eval(blist[2])))
print("A.B =", adotb)

#norm
anorm = (math.sqrt(eval(alist[0])**2 + eval(alist[1])**2 + eval(alist[2])**2))
rndanorm = round(anorm,2)
print("|A| =", "{0:0<4}".format(rndanorm))

bnorm = (math.sqrt(eval(blist[0])**2 + eval(blist[1])**2 + eval(blist[2])**2))
rndbnorm = round(bnorm,2)
print("|B| =", "{0:0<4}".format(rndbnorm))
