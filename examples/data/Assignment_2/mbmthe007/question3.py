
pi=0
for k in range(18):
    pi+=(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))/16**k
x=round(pi,3)
print("Approximation of pi:", end=' ')
print(x,end='')
        


y=eval(input("\nEnter the radius:\n"))
a=pi*(y**2)
z=round(a, 3)
print("Area:", end=' ')
print(z,end='')
