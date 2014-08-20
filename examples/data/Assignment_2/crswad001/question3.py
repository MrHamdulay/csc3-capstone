import math
next=math.sqrt(2)
nextterm=2
cumu=2
while nextterm!=1:
    nextterm = 2/next
    cumu *= nextterm
    next= math.sqrt(2+next)
cumur = round(cumu,3)
print("Approximation of pi:",cumur)
radi = eval(input("Enter the radius:\n"))
print("Area:",round(radi*radi*cumu,3))


