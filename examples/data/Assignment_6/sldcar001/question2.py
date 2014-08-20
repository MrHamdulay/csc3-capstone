import math
def mag(a,b,c):
    a=math.sqrt(a**2+b**2+c**2)
    return(a)
def vector(x,y,z,bx,by,bz):
    ax,ay,az,bx,by,bz=eval(x),eval(y),eval(z),eval(bx),eval(by),eval(bz)
    Csum=[]
    cx,cy,cz=ax+bx,ay+by,az+bz
    Csum.append(cx)
    Csum.append(cy)
    Csum.append(cz)
    output="{0:4}= {1}"
    out="{0:4}= {1:.2f}"
    print(output.format("A+B",Csum))
    Cdot=ax*bx+ay*by+az*bz
    print(output.format("A.B",Cdot))
    a=mag(ax,ay,az)
    print(out.format("|A|",a))
    b=mag(bx,by,bz)
    print(out.format("|B|",b))
    
def get():
    A=input("Enter vector A:\n")
    Ax,Ay,Az=A.split()
    B=input("Enter vector B:\n")
    Bx,By,Bz=B.split()
    vector(Ax,Ay,Az,Bx,By,Bz)
    
get()

