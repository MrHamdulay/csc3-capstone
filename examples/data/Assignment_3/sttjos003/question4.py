import math

x=eval(input("Enter the starting point N:\n"))+1
y=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

while x<y:
    d=str(x)
    if d==d[::-1]:
        c=math.sqrt(x)
        c=round(c)+1
       
        if x==2 or x==3:
            print(x)
        elif x>3:
            p=2
            while p<c+1:
                if x%p!=0:
                    p+=1
                else: break
            if p==c+1:
                print(x)
                   
        x=x+1
    else:
        x=x+1
        continue