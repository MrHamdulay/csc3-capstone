#ASSIGNMENT_4
#QUESTION_4
#ASIL_MOTALA
#MTLASI002
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(n+1,m):
    x=str(i)
    if x==x[::-1]:
        a=1
        if a==1 and i==2:
            print(i)
        for j in range(1,i):
            if j==1:
                continue
            elif i%j==0:
                a=1
                break
            else:
                a=2
        if a==1:
            continue
        elif a==2:
            print(i)        