x=2
n=2
b=2
d=2**.5
while b>1:
    n=n**.5
    b=2/n
    c=x*b
    x=c
    n=2+d
    d=(2+d)**.5
print("Approximation of pi:",round(c,3))
print("Enter the radius:")
f=eval(input())
area=c*(f**2)
print("Area:",round(area,3))