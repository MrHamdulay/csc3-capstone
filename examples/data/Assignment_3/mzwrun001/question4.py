n=eval(input("Enter the starting point N:""\n"))
m=eval(input("Enter the ending point M:""\n"))
#n+=1
#print("The palindrome:")
#in each iteration there are some values which are not divisible by other numbers like 303/2
print("The palindromic primes are:")
for q in range (n+1,m) :
    for p in range(2,q):
        if q%p==0 :
            break
            #if str(i)==str(i)[::-1]:
             #   break
    else:
        x=str(q)
        y=x[::-1]
        if x==y:
            #str(i)==str(i)[::-1]
            print(q)
            
            