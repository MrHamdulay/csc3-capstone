#question2

d=eval(input("Enter the height of the triangle:\n"))
for i in range(d+1):
    if i!=0:
        print(" "*(d-i),"*"*(2*i-1),sep="")
    else:
        continue
    