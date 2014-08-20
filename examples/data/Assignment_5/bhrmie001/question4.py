import math
z=input("Enter a function f(x):\n")
yinc=1/20
for y in range(-10, 11):
    for x in range(-10, 11):
        if z.find("**") == True or z.find("**")==0:
            if x<0:
                x=-x
        k="("+str(x)+")"
        f=z.replace("x", k)        

        f=eval(f)
        x_real=f/10
        y_real=-y/10
        if y_real-yinc<=x_real<=y_real+yinc:
            print("o", end="")
        elif x==0 and y==0:
            print("+", end="")
        elif x==0:
            print("|", end="")
        elif y==0:
            print("-", end="")
        else:
            print(" ", end="")
    print()