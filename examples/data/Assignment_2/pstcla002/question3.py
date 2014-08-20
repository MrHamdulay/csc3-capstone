# Assignment 2 question 3
# Pi and Area appoximation
def pi():
    import math
    #next=denominator
    #nextterm= next whole term
    #acu= cumulated value
    next=math.sqrt(2)
    nextterm=2
    acu=2
    while nextterm !=1:
        nextterm=2/next
        acu= acu*nextterm
        next=math.sqrt(2+next)
    acu_r=round(acu,3)
    print("Approximation of pi:", acu_r)
    radi=eval(input("Enter the radius: \n"))
    print("Area:", round(radi*radi*acu, 3))
    
pi()