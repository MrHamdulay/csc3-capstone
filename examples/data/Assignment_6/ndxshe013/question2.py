import math

def add(a,b):
    return [a[i]+b[i] for i in range(3)]
def multiply(a,b):
    x =0
    for i in range(3):
        x += a[i]*b[i]
    return x
def le(x):
    return math.sqrt(x[0]**2 + x[1]**2 + x[2]**2)
def main():
    x = input("Enter vector A:\n").split()
    y = input("Enter vector B:\n").split()

    x = [eval(i) for i in x]
    y = [eval(i) for i in y]

    print("A+B =",add(x,y))
    print("A.B =",multiply(x,y))
    print("|A| =","{:.2f}".format(le(x)))
    print("|B| =","{:.2f}".format(le(y)))
main()
