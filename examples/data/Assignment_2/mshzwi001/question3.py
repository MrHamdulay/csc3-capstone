# a program to calculate the area of a circle
# mashau zwivhuya
# 9 march 2014
def main():
    a=(2**(1/2))
    b=((2+a)**(1/2))
    c=((2+b)**(1/2))
    d=((2+c)**(1/2))
    e=((2+d)**(1/2))
    f=((2+e)**(1/2))
    g=((2+f)**(1/2))
    h=((2+g)**(1/2))
    i=((2+h)**(1/2))
    j=((2+i)**(1/2))
    k=((2+j)**(1/2))
    pi=2*(2/a)*(2/b)*(2/c)*(2/d)*(2/e)*(2/f)*(2/g)*(2/h)*(2/i)*(2/j)*(2/k)
    print("Approximation of pi:",round(pi,3))
    z=eval(input("Enter the radius:\n"))
    area=pi*(z)**2
    print("Area:",round(area,3))
    
main()  