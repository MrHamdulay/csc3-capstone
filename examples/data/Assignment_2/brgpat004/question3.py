import math

def nextterm(term):
    termstring="math.sqrt(2"
    for i in range(term-1):
        termstring=termstring+"+math.sqrt(2"
    termstring=termstring+")"*term

    return 2/eval(termstring)

pi=2
count=1
endloop=0
while endloop!=1:
    
    pi=pi*nextterm(count)
    endloop=nextterm(count)
    count+=1
    
    
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
print("Area:",round(pi*radius**2,3))

